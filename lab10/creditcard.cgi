#!/usr/bin/perl -w
# validate a credit card number by calculating its
# checksum using Luhn's formula (https://en.wikipedia.org/wiki/Luhn_algorithm)

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html("Credit Card Validation"), "\n";
warningsToBrowser(1);
$credit_card = param("credit_card");
if (defined $credit_card) {
	if (defined param('Validate')){
		$result = validate($credit_card); 
		if ( $result =~ /\bvalid\b/){
			print h2(validate($credit_card)),"\n";
			param('credit_card',''),"\n";
			print start_form,"\n";
			print "Enter ANOTHER card number:\n",textfield(-name =>'credit_card'),"\n";
			print submit('Validate'), "\n";
			print submit('Reset'), "\n";
			print submit('Close'), "\n";
			print end_form, "\n";
		}else{
			#invalid
			print h2(validate($credit_card)),"\n";
			param('credit_card',''),"\n";
			print start_form,"\n";
			print "Try again, card number:\n",textfield('credit_card'),"\n";
			print submit('Validate'), "\n";
			print submit('Reset'), "\n";
			print submit('Close'), "\n";
			print end_form, "\n";
		}
	}elsif(defined param('Reset')){
		param('credit_card',''),"\n";
		print h2('Credit Card Validation'); 
		print "This page checks whether a potential credit card number satisfies the Luhn Formula.\n";
		print start_form,"\n";
		print "Enter credit card number:\n",textfield('credit_card'),"\n";
		print submit('Validate'), "\n";
		print submit('Reset'), "\n";
		print submit('Close'), "\n";
		print end_form, "\n";
	}elsif(defined param('Close')){
		print h2("Goodbye, have a good day!\n");
	}else{
		print "3\n";		
	}
}else{
	print h2('Credit Card Validation'),"\n"; 
	print "This page checks whether a potential credit card number satisfies the Luhn Formula.\n";
	print start_form,"\n";
	print "Enter credit card number:\n",textfield('credit_card'),"\n";
	print submit('Validate'), "\n";
	print submit('Reset'), "\n";
	print submit('Close'), "\n";
	print end_form, "\n";
}

print end_html;
exit 0;


sub luhn_checksum{
	my ($no) = @_;
	my $checksum = 0;
	my @digits = reverse(split //, $no);
	foreach $index (0..$#digits){
		$multipliter = 1 + $index % 2;
		$digit = $digits[$index] * $multipliter;
		if ($digit > 9){
			$digit -= 9;
		}
		$checksum += $digit;
	}
	return $checksum;
}

sub validate{
	my ($credit_no) = @_;
	$credit_no =~ s/</&lt;/g; # for avoiding to XSS
	my $no = $credit_no;
	$no =~ s/\D//g;
	if(length $no != 16){
		return "$no is invalid - does not contain exactly 16 digits\n";
	}elsif(luhn_checksum($no) % 10 == 0){
		return "$no is valid\n";
	}else{
		return "$no is invalid\n";
	}	
}

