#!/bin/sh

echo Content-type: text/html
echo

host_name=`host "$REMOTE_ADDR"|sed 's/.*\s//'|sed 's/.$//'`
identifies=`echo "$HTTP_USER_AGENT"|sed 's/.*=\s//'`

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>IBrowser IP, Host and User Agent</title>
</head>
<body>
Your browser is running at IP address: <b>$REMOTE_ADDR</b>
<p>
Your browser is running on hostname: <b>$host_name</b>
</p><p>
Your browser identifies as: <b>$identifies</b>
</p>
</body>
</html>
eof
