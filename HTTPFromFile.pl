#!/usr/bin/perl
use strict;
use warnings;
use feature qw(say);

use LWP::UserAgent;
use HTTP::Request;
use HTTP::Response;

use Getopt::Long;


#parameter defined
my $response_code = 403;
my $request_file = q{};
my $host = "127.0.0.1";
my $port = 80;
my $help = q();

# Forces flushing of STDOUT without waiting for EOL
$| = 1;


GetOptions(
	'h|help'=>\$help,
	'code=i'=>\$response_code,
	'file=s'=>\$request_file,
	'host=s'=>\$host,
	'port=i'=>\$port,
);

sub getHelp{
	print <<__HELP__;
Usage: perl $0 [-code 403] [-host 127.0.0.1] [-port 80] -file request_file_path

-code: Specify the expected reponse code
-host: Specify the host to send request
-port: Specify the port to send request
-file: Specify the request content file path

__HELP__
}

if($help){
	getHelp();
	exit 0;
}

die "You need to specify the request content file path \nPlease run --help for more help " unless -e $request_file;

chomp $request_file;
chomp $host;
chomp $port;
chomp $response_code;

sendRequest();


sub sendRequest{
	my $file = `cat $request_file`."\r\n";

	my $request = HTTP::Request->parse($file);

	$request->uri("http://$host:$port" . $request->uri);

	#if no ua from t file ,set ua null
	my $ua = LWP::UserAgent->new;
	$ua->show_progress(1);
	$ua->agent('') unless defined($request->header('User-Agent'));


	#send request
	my $response = $ua->request($request);
	
	die "Can't parse response $response\n" unless defined( $response );

	#ok: is the response_code expected
	my $ok = 1;

	$ok = 0 if $response->code != $response_code;

	print $request->as_string;
	print $response->as_string;

	$ok ? say "OK" : say "Not OK";

	return $ok;
}

