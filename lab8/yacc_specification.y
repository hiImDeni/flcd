%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1 
%}

%token AND
%token OR
%token NOT
%token IF
%token THEN
%token ELSE
%token WHILE
%token DO
%token READ
%token WRITE
%token INT
%token NONE
%token STRING
%token CHAR
%token BOOL
%token REAL
%token RETURN
%token IDENTIFIER
%token CONSTANT
%token SEMI_COLON
%token COMMA
%token DOT
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_SQUARE_BRACKET
%token CLOSED_SQUARE_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token PLUS
%token MINUS
%token MUL
%token DIV
%token PERCENT
%token LT
%token GT
%token ATRIB
%token EQ
%token NOT_EQ

%left '+' '-' '*' '/' '%'
%left '!' '&' '|'

%%

structured_stmt : '[' compound_stmt ']' {printf("structured stmt\n");}
				;
				
compound_stmt : stmt {printf("stmt\n");}
			  | compound_stmt '.' stmt {printf("compound stmt\n");}
              ;

stmt : assign_stmt {printf("assign stmt\n");}
	 | if_stmt {printf("if stmt\n");}
	 | while_stmt {printf("while stmt\n");}
	 | expr '.' {printf("expr\n");}
	 ;
	 
expr : expr '+' expr
	 | expr '-' expr
	 | expr '*' expr
	 | expr '/' expr
	 | expr '%' expr
	 | expr '&' expr
	 | expr '|' expr
	 | '!'
	 | '(' expr ')'
	 | '[' expr ']'
	 | '{' expr '}'
	 
assign_stmt : IDENTIFIER ':=' expr
			| IDENTIFIER ':=' IDENTIFIER '.'
			;
			
if_stmt : IF condition THEN structured_stmt 
        | IF condition THEN structured_stmt ELSE structured_stmt
        ;

while_stmt : WHILE condition DO structured_stmt
           ;

condition : expr relational_operator expr conditional_operator condition 
          | NOT expr relational_operator expr conditional_operator condition 
          | expr relational_operator expr 
          | NOT expr relational_operator expr
		  ;
		  
relational_operator : '<' | '>' | '=';
conditional_operator : '&' | '|'

%%


yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"No errors detected\n");
}