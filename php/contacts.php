<?php

/*
  |--------------------------------------------------------------------------
  | Mailer module
  |--------------------------------------------------------------------------
  |
  | These module ares used when sending email from contact form
  |
 */


/* SECTION I - CONFIGURATION */

$receiver_mail = 'example@mail.com';
$mail_title    = ( !empty( $_POST[ 'website' ] )) ? $_POST[ 'name' ] . ' from ' . $_POST[ 'website' ] : ' from [WebSite]';

/* SECTION II - CODE */

if ( !empty( $_POST[ 'name' ] ) && !empty( $_POST [ 'e-mail' ] ) && !empty( $_POST [ 'message' ] ) ) {
    $email   = $_POST[ 'name' ] . '<' . $_POST[ 'e-mail' ] . '>';
    $message = wordwrap( $_POST[ 'message' ], 70, "\r\n" );
    if(!empty($_POST[ 'website' ]))
        $message .= "\r\n\r\n".'Website: '.$_POST['website'];
    $subject = $mail_title;
    $header = 'From: '. $email . "\r\n";
    $header = 'Reply-To: ' . $email;
    if ( mail( $receiver_mail, $subject, $message, $header ) )
        $result = 'Message successfully sent.';
    else
        $result = 'Message could not be sent.';
} else {
    $result  = 'Please fill all the fields in the form.';
}
echo $result;