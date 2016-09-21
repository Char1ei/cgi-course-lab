#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html('Login');
warningsToBrowser(1);

$username = param('username') || '';
$password = param('password') || '';

if ($username && $password) {
	if (!open F, "<accounts/$username/password"){
		print "unknown username!\n";
	} else {
		$correct_password=<F>;
		chomp $correct_password;	
		if ($password eq $correct_password){
			print "$username authenticated.\n";
		} else {
			print "incorrect_password!\n";
		}
	}
}elsif(!$username && $password){
	print "Enter username\n";
	print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
	print "Password:\n",textfield(password => "$password"), "\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
}elsif($username && !$password){
	print "Enter Password\n";
	print start_form, "\n";
    print "Username:\n", textfield(username => "$username"),"\n";
    print "Password:\n", textfield('password'),"\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
} else {
    print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
    print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
}
print end_html;
exit(0);
