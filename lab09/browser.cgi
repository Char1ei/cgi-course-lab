#!/bin/sh

echo Content-type: text/html
echo

host_name=`host "$HTTP_X_FORWARDED_FOR" |sed 's/.*\s//'|sed 's/.$//'`
identifies=`echo "$HTTP_USER_AGENT"|sed 's/.*=\s//'`

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>Webserver IP, Host and Software</title>
</head>
<body>
Your browser is running at IP address: <b>$HTTP_X_FORWARDED_FOR</b>
<p>
Your browser is running on hostname: <b>$host_name</b>
<p>
Your browser identifies as: <b>$identifies</b>
</body>
</html>
eof
