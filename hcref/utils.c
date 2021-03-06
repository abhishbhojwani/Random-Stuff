/******************************************************************************\
 *                                 U T I L S . C                              *
 *                                ===============                             *
 *                                                                            *
 *      This file contains the utility routines for the hcref program.        *
 *                                                                            *
\******************************************************************************/

#include "portable.h"

#include "utils.h"

/*******************************************************************************
       Name : HTML_bodyheader()
Description : Write out a HTML header to an open file.
 Parameters : out_file - FILE * pointer to open file
            : status   - string holding string for status line
    Returns :
   Comments :
*******************************************************************************/
void
HTML_bodyheader(FILE *out_file, char *status)
{
    fprintf(out_file, "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">\n");
    fprintf(out_file, "<!-- Generated by hcref %d.%d -->\n", VERSION, RELEASE);
    fprintf(out_file, "<HTML>\n");
    fprintf(out_file, "  <HEAD>\n");
    fprintf(out_file, "    <META http-equiv=\"Content-Type\" "
                      "content=\"text/html; charset=iso-8859-1\">\n");
    fprintf(out_file, "    <title>hcref Output</title>\n");
    fprintf(out_file, "  </HEAD>\n");
    fprintf(out_file, "  <BODY ONLOAD=\"window.defaultStatus='%s';\" "
                      "LEFTMARGIN=\"%d\" TOPMARGIN=\"%d\">\n",
                      status, DEF_LEFTMARGIN, DEF_TOPMARGIN);
}


/*******************************************************************************
       Name : HTML_bodyfooter()
Description : Write out a HTML footer to an open file.
 Parameters : out_file - FILE * pointer to open file
    Returns :
   Comments :
*******************************************************************************/
void
HTML_bodyfooter(FILE *out_file)
{
    fprintf(out_file, "  </BODY>\n");
    fprintf(out_file, "</HTML>\n");
}

