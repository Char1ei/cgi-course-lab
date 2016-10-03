#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

$run_env = `env`;

if($run_env =~ /GATEWAY_INTERFACE=CGI/){
	# running on CGI
	print header, start_html('Login');
	warningsToBrowser(1);

	if (defined param('username') && defined param('password')) {
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
	}elsif(defined param('password')){
		print "Enter username\n";
		print start_form, "\n";
	    print "Username:\n", textfield('username'), "\n";
		print hidden(-name => "password", -default => "$password"), "\n";
	    print submit(value => Login), "\n";
	    print end_form, "\n";
	}elsif(defined param('username')){
		print "Enter Password\n";
		print start_form, "\n";
		print hidden(-name => "username", -default => "$username"), "\n";
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
}else{
	# running on command line
	print "username: ";
	$username = <stdin>;
	chomp $username;
	print "password: ";
	$password = <stdin>;
	chomp $password;
	# adjust username
	$username = substr $username, 0 , 256;
	$username =~ s/\W//g;

	$password_file = "accounts/$username/password";
	if (!open F, "<$password_file"){
		print "unknow username!\n";
	}else{
		$correct_pass = <F>;
		chomp $correct_pass;
		if ($password eq $correct_pass){
			print "You are authenticated.\n";
		}else{
			print "incorrect password!";
		}
	}
}
