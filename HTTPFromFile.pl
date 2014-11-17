#!/usr/bin/perl
use strict;
use warnings;
use feature qw(say);

use LWP::UserAgent;
use HTTP::Request;
use HTTP::Response;

use Getopt::Long;


#parameter defined
my $uri = "127.0.0.1";
my $response_code = 403;
my $request_file = q{};
my $host = "localhost";
my $port = 80;
my $help = q();
my $dir = q();

# Forces flushing of STDOUT without waiting for EOL
$| = 1;


GetOptions(
	'h|help'=>\$help,
	'code=i'=>\$response_code,
	'file=s'=>\$request_file,
	'host=s'=>\$host,
	'port=i'=>\$port,
	'dir=s'=>\$dir,
	'uri=s'=>\$uri,
);

sub getHelp{
	print <<__HELP__;
Usage: perl $0 [-code 403] [-uri 127.0.0.1] [-host example.com] [-port 80] -file request_file_path

-code: Specify the expected reponse code
-uri: Specify the domain or host ip to send request,default is 127.0.0.1
-host: Specify the Host header,default is localhost
-port: Specify the port to send request,default is 80
-file: Specify the request content file path
-dir: Specify the dir path for all t files

__HELP__
}

if($help){
	getHelp();
	exit 0;
}

die "You need to specify the exists request content file path for single t file\nPlease run --help for more help " if ( not -e $request_file and not $dir) ;

die "You need to specify the exists t file dir for all t files test\nPlease run --help for more help " if $dir and not -e $dir;

chomp $request_file;
chomp $uri;
chomp $host;
chomp $port;
chomp $response_code;

sendRequest($request_file) unless $dir;

sendTotal() if $dir and -e $dir;

sub sendRequest{
	my $request_file = shift; 
	
	$uri = $host if $uri  eq "127.0.0.1";

	my $file = `cat $request_file`."\r\n";

	my $request = HTTP::Request->parse($file);

	$request->uri("http://$uri:$port" . $request->uri);

	$request->header("Host" => $host);
        $request->header("Referer" => "http://$host:$port") unless defined($request->header('Referer'));
	$request->header("Accept" => "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8") unless defined($request->header('Accept'));
	$request->header("Accept-Encoding" => "gzip,deflate,sdch") unless defined($request->header('Accept-Encoding'));
	$request->header("Accept-Language" => "zh-CN,zh;q=0.8,en;q=0.6") unless defined($request->header('Accept-Language')); 
	
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
	print $response->headers_as_string;
	print "\n$request_file \t";
	$ok ? say $response->code." OK" : say $response->code." Not OK";
	print "************************************************************\n";

	return $ok;
}

sub sendTotal{
	my $pass = 0;
	my $fail = 0;
	my @failures = q();

	my @t_dirs = glob "${dir}/*.t";

	foreach my $t (@t_dirs) {
		if (sendRequest($t)){
			$pass += 1;
                } else{
                        $fail += 1;
			push @failures, $t;
		}
	}
	print "ALL Done \n";
        
	my $total = $pass + $fail;

	print "ran $total tests: $pass passed; $fail failed \n";

	if ($fail > 0){
		foreach my $t (@failures) {
			print "Failed: $t\n";
		}
		exit 1;
	}
}
