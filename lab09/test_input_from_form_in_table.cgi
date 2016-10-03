#!/usr/bin/perl

print "Content-type: text/html

<html>
<head></head>
<body>
<h2>Input Parameters</h2>
<hr>",
"<form method='get' action='test_dispaly_input_from_form_in_table.cgi'>",
"A=","
<input type='text' name='a'>
<input type='submit'>
</form>",
"<form method='post' action='test_dispaly_input_from_form_in_table.cgi'>",
"B=","
<input type='text' name='b'>
<input type='submit'>
</form>
<pre>";

# if ($ENV{REQUEST_METHOD} eq 'POST') {
#     $parameters = <>;
# } else {
#     $parameters = $ENV{QUERY_STRING}
# }
#
# foreach (split(/\&/, $parameters)) {
#     /([^=]*)=(.*)/;
#     print "<tr><td>$1<td>$2\n";
# }

print "
</pre>
<hr>
</body>
</html>
";

