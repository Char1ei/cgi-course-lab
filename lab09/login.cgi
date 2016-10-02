 #!/usr/bin/perl -w
2	2
 
3	3
 use CGI qw/:all/;
4	4
 use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
5	5
 
6	6
 print header, start_html('Login');
7	7
 warningsToBrowser(1);
8	8
 
9	9
 $username = param('username') || '';
10	10
 $password = param('password') || '';
11	11
 
12	12
 if ($username && $password) {
13	13
 	if (!open F, "<accounts/$username/password"){
14	14
 		print "unknown username!\n";
15	15
 	} else {
16	16
 		$correct_password=<F>;
17	17
 		chomp $correct_password;	
18	18
 		if ($password eq $correct_password){
19	19
 			print "$username authenticated.\n";
20	20
 		} else {
21	21
 			print "incorrect_password!\n";
22	22
 		}
23	23
 	}
24	24
 }elsif(!$username && $password){
 	print "Enter username\n";
 	print start_form, "\n";
     print "Username:\n", textfield('username'), "\n";
 	print "Password:\n",textfield(password => "$password"), "\n";
 	print hidden(-name => "password", -default => "$password"), "\n";
     print submit(value => Login), "\n";
     print end_form, "\n";
 }elsif($username && !$password){
 	print "Enter Password\n";
 	print start_form, "\n";
     print "Username:\n", textfield(username => "$username"),"\n";
 	print hidden(-name => "username", -default => "$username"), "\n";
     print "Password:\n", textfield('password'),"\n";
     print submit(value => Login), "\n";
     print end_form, "\n";
38	38
 } else {
39	39
     print start_form, "\n";
40	40
     print "Username:\n", textfield('username'), "\n";
41	41
     print "Password:\n", textfield('password'), "\n";
42	42
     print submit(value => Login), "\n";
43	43
     print end_form, "\n";
44	44
 }
45	45
 print end_html;
46	46
 exit(0);
