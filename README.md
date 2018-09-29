# if_StreamlabsParameter

An if-else parameter for streamlabs chatbot

## Requirements

You need python scripting set up for Streamlabs Chatbot.  This means you must
have Python 2.7.13 installed.  There are tutorials available online for
installing Python and configuring Streamlabs Chatbot to use it.

## Installation

You can download the .ZIP file for this script from the repository page at
https://github.com/madelsberger/if_StreamlabsParameter

(Near the top right of the page, click the **Clone or Download** button; in the
pop-up, click **Download ZIP**.)

Then on the Scripts tab in Streamlabs Chatbot, click the import button (an
"arrow-pointing-into-a-box" icon near the upper right of the screen) and select
the downloaded zip file.

The script list should now include *if*; check the **Enabled** box for this
script, and it will be ready to use in commands.

## Usage

Once you import this script, you can use the $if parameter in your commands.  
The parameter syntax is

    $if('<expr>', '<true-message>', '<false-message>')

For example

    $if('5 > 3', 'Good', 'Uhoh')

will print *Good*

`<expr>`, `<true-message>`, and `<false-message>` must be enclosed in single
quotes (').  If you need to use single-quotes within one of the values, escape
them with *\* as in

    $if('5 > 3', 'It\'s good', 'Uhoh')

`<expr>` is evaluated (by Python).  If it returns a "true" value (True, a 
non-0 number, etc.) then the parameter returns `<true-message>`.  If it 
returns a "false" value (None, False, 0, "", etc.) then the parameter returns 
`<false-message>`.  If there's an error evaluating `<expr>`, or if the
parameter syntax is incorrect, then the parameter is left as-is in the message
string.

The real power of $if comes from combining it with other parameters.  You can
embed any parameter recognzied by the bot in your expression; Python will
evaluate the expression after the parameter has been substituted.

    $if('$points > 1000', 'You have a lot of points', '')

If the evaluated response string is 0-length, no message is sent, so a command 
with this response will say *You have a lot of points* only if the user
invoking it has more than 1000 points.

Note that in `<expr>` string values must be enclosed in quotes (since the
expression is interpreted as Python code), as in 

    $if('"$user" == "fred"', 'Hi, Fred!', 'Who are you?')

## Programmer's Note

Sorry for the quick-and-dirty state of the code; maybe I'll clean it up some
day.
