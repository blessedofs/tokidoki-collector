#!/usr/bin/env python3
"""One-click safe importer: discover public candidate images, import only authorized exact matches."""
import csv, json, re, sys, urllib.request, urllib.parse, html
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCES={"Series 1":"https://www.kayouofficial.com/en-UK/series/series-x0wyu07i","Series 2":"https://www.kayouofficial.com/en-US/series/series-ppqnqj4k"}
HEADERS={'User-Agent':'BHSCollectorLibrary/1.0 (catalog image source review)'}
class Images(HTMLParser):
 def __init__(self):super().__init__();self.results=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='img':
   for key in ('src','data-src','data-original','srcset'):
    v=a.get(key,'')
    if v:
     self.results.append((a.get('alt','').strip(),v.split(',')[0].strip().split(' ')[0]))
  if tag=='meta' and a.get('property') in ('og:image','twitter:image'):
   self.results.append(('page preview',a.get('content','')))
def discover():
 rows=[]
 for series,url in SOURCES.items():
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers=HEADERS),timeout=20) as resp:
    data=resp.read(3_000_000).decode('utf-8','replace')
   parser=Images();parser.feed(data)
   for alt,img in parser.results:
    absolute=urllib.parse.urljoin(url,html.unescape(img))
    if urllib.parse.urlparse(absolute).scheme=='https':rows.append([series,alt,absolute,url])
   print(series,'candidate URLs:',len(parser.results))
  except Exception as e:print('Discovery unavailable for',series,str(e),file=sys.stderr)
 with (ROOT/'candidate-images.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(['series','image_alt','candidate_url','catalog_url']);w.writerows(dict.fromkeys(map(tuple,rows)))
 print('Candidate report saved. Candidates are NOT automatically matched or published.')
def import_approved():
 path=ROOT/'image-sources.csv'; cards=json.loads((ROOT/'cards.json').read_text());by_id={c['id']:c for c in cards};imported=0
 with path.open(newline='',encoding='utf-8') as f:
  for row in csv.DictReader(f):
   cid=row.get('card_id','').strip();url=row.get('image_url','').strip();permission=row.get('permission_confirmed','').strip().lower()
   if not cid or not url:continue
   if permission not in ('yes','true'):print('SKIP permission unconfirmed:',cid);continue
   if cid not in by_id:print('SKIP unknown ID:',cid);continue
   parsed=urllib.parse.urlparse(url)
   if parsed.scheme!='https' or not parsed.hostname:print('SKIP invalid HTTPS URL:',cid);continue
   try:
    req=urllib.request.Request(url,headers=HEADERS)
    with urllib.request.urlopen(req,timeout=25) as response:
     content_type=response.headers.get('Content-Type','').split(';')[0].lower()
     ext={'image/jpeg':'.jpg','image/png':'.png','image/webp':'.webp','image/gif':'.gif'}.get(content_type)
     if not ext:raise ValueError('Unsupported content type '+content_type)
     blob=response.read(6_000_001)
     if len(blob)>6_000_000:raise ValueError('Image larger than 6 MB')
    filename=re.sub('[^A-Za-z0-9_-]','-',cid)+ext
    dest=ROOT/'assets'/filename;dest.parent.mkdir(exist_ok=True);dest.write_bytes(blob)
    by_id[cid]['image']='assets/'+filename
    imported+=1;print('IMPORTED:',cid)
   except Exception as e:print('FAILED:',cid,str(e),file=sys.stderr)
 if imported:
  (ROOT/'cards.json').write_text(json.dumps(cards,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print('Imported',imported,'approved card images; existing artwork preserved.')
if __name__=='__main__':
 discover()
 import_approved()
