#include "ssetcolor.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

struct ssc_style {
    char codes[256];
    int len;
};

#define ANSI_RESET "\033[0m"

int ssc_supports_color(void) {
#ifdef _WIN32
    static int checked = 0, support = 0;
    if (!checked) {
        HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
        if (h != INVALID_HANDLE_VALUE) {
            DWORD mode = 0;
            if (GetConsoleMode(h, &mode)) support = 1;
        }
        checked = 1;
    }
    return support;
#else
    return isatty(fileno(stdout));
#endif
}

int ssc_color_depth(void) {
#ifdef _WIN32
    return 16;
#else
    char* ct = getenv("COLORTERM");
    if (ct) {
        if (strstr(ct, "truecolor") || strstr(ct, "24bit"))
            return 16777216;
    }
    char* t = getenv("TERM");
    if (t) {
        if (strstr(t, "256")) return 256;
        if (strstr(t, "color")) return 16;
    }
    return ssc_supports_color() ? 16 : 0;
#endif
}

ssc_style_t* ssc_style_new(void) {
    ssc_style_t* s = (ssc_style_t*)calloc(1, sizeof(ssc_style_t));
    if (s) { s->len = 0; s->codes[0] = '\0'; }
    return s;
}

void ssc_style_free(ssc_style_t* s) { free(s); }

void ssc_style_add(ssc_style_t* s, const char* code) {
    if (!s || !code) return;
    int slen = (int)strlen(code);
    if (s->len + slen < (int)sizeof(s->codes) - 1) {
        memcpy(s->codes + s->len, code, slen);
        s->len += slen;
        s->codes[s->len] = '\0';
    }
}

void ssc_style_add_fg(ssc_style_t* s, const char* c) {
    if (!s || !c) return;
    char b[32];
    if (strcmp(c,"black")==0) snprintf(b,sizeof(b),"\033[30m");
    else if (strcmp(c,"red")==0) snprintf(b,sizeof(b),"\033[31m");
    else if (strcmp(c,"green")==0) snprintf(b,sizeof(b),"\033[32m");
    else if (strcmp(c,"yellow")==0) snprintf(b,sizeof(b),"\033[33m");
    else if (strcmp(c,"blue")==0) snprintf(b,sizeof(b),"\033[34m");
    else if (strcmp(c,"magenta")==0) snprintf(b,sizeof(b),"\033[35m");
    else if (strcmp(c,"cyan")==0) snprintf(b,sizeof(b),"\033[36m");
    else if (strcmp(c,"white")==0) snprintf(b,sizeof(b),"\033[37m");
    else return;
    ssc_style_add(s,b);
}

void ssc_style_add_bg(ssc_style_t* s, const char* c) {
    if (!s || !c) return;
    char b[32];
    if (strcmp(c,"black")==0) snprintf(b,sizeof(b),"\033[40m");
    else if (strcmp(c,"red")==0) snprintf(b,sizeof(b),"\033[41m");
    else if (strcmp(c,"green")==0) snprintf(b,sizeof(b),"\033[42m");
    else if (strcmp(c,"yellow")==0) snprintf(b,sizeof(b),"\033[43m");
    else if (strcmp(c,"blue")==0) snprintf(b,sizeof(b),"\033[44m");
    else if (strcmp(c,"magenta")==0) snprintf(b,sizeof(b),"\033[45m");
    else if (strcmp(c,"cyan")==0) snprintf(b,sizeof(b),"\033[46m");
    else if (strcmp(c,"white")==0) snprintf(b,sizeof(b),"\033[47m");
    else return;
    ssc_style_add(s,b);
}

void ssc_style_add_fg_256(ssc_style_t* s, int c) {
    if (!s) return;
    char b[24]; snprintf(b,sizeof(b),"\033[38;5;%dm",c);
    ssc_style_add(s,b);
}

void ssc_style_add_bg_256(ssc_style_t* s, int c) {
    if (!s) return;
    char b[24]; snprintf(b,sizeof(b),"\033[48;5;%dm",c);
    ssc_style_add(s,b);
}

void ssc_style_add_fg_rgb(ssc_style_t* s, int r, int g, int b) {
    if (!s) return;
    char buf[32]; snprintf(buf,sizeof(buf),"\033[38;2;%d;%d;%dm",r,g,b);
    ssc_style_add(s,buf);
}

void ssc_style_add_bg_rgb(ssc_style_t* s, int r, int g, int b) {
    if (!s) return;
    char buf[32]; snprintf(buf,sizeof(buf),"\033[48;2;%d;%d;%dm",r,g,b);
    ssc_style_add(s,buf);
}

int ssc_style_apply_buf(char* buf, int sz, const ssc_style_t* s, const char* t) {
    if (!buf || sz<=0 || !t) return 0;
    if (s && s->len>0) return snprintf(buf,sz,"%s%s%s", s->codes, t, ANSI_RESET);
    return snprintf(buf,sz,"%s", t);
}

char* ssc_style_apply(const ssc_style_t* s, const char* t) {
    if (!t) return NULL; int need;
    if (s && s->len>0) need = s->len + (int)strlen(t) + (int)strlen(ANSI_RESET) + 1;
    else need = (int)strlen(t) + 1;
    char* r = (char*)malloc(need);
    if (!r) return NULL; ssc_style_apply_buf(r,need,s,t); return r;
}

int ssc_wrap_buf(char* buf, int sz, const char* t, const char* c) {
    if (!buf || sz<=0 || !t) return 0;
    if (c) return snprintf(buf,sz,"%s%s%s",c,t,ANSI_RESET);
    return snprintf(buf,sz,"%s",t);
}

char* ssc_wrap(const char* t, const char* c) {
    if (!t) return NULL;
    int an = c ? (int)strlen(c) : 0;
    int rl = (int)strlen(ANSI_RESET);
    int tl = (int)strlen(t);
    int need = an + tl + rl + 1;
    char* r = (char*)malloc(need);
    if (!r) return NULL; ssc_wrap_buf(r,need,t,c); return r;
}

void ssc_free(char* p) { free(p); }

#define WRAP(name,code) char* ssc_##name(const char* t) { return ssc_wrap(t,code); }

WRAP(bold, SSC_BOLD)
WRAP(fade, SSC_FADE)
WRAP(italic, SSC_ITALIC)
WRAP(underline, SSC_UNDERLINE)
WRAP(blink_slow, SSC_BLINK_SLOW)
WRAP(blink_fast, SSC_BLINK_FAST)
WRAP(reverse, SSC_REVERSE)
WRAP(hidden, SSC_HIDDEN)
WRAP(concealed, SSC_CONCEALED)

WRAP(black, SSC_BLACK)
WRAP(red, SSC_RED)
WRAP(green, SSC_GREEN)
WRAP(yellow, SSC_YELLOW)
WRAP(blue, SSC_BLUE)
WRAP(magenta, SSC_MAGENTA)
WRAP(cyan, SSC_CYAN)
WRAP(white, SSC_WHITE)

WRAP(bg_black, SSC_BG_BLACK)
WRAP(bg_red, SSC_BG_RED)
WRAP(bg_green, SSC_BG_GREEN)
WRAP(bg_yellow, SSC_BG_YELLOW)
WRAP(bg_blue, SSC_BG_BLUE)
WRAP(bg_magenta, SSC_BG_MAGENTA)
WRAP(bg_cyan, SSC_BG_CYAN)
WRAP(bg_white, SSC_BG_WHITE)

WRAP(bright_black, SSC_BRIGHT_BLACK)
WRAP(bright_red, SSC_BRIGHT_RED)
WRAP(bright_green, SSC_BRIGHT_GREEN)
WRAP(bright_yellow, SSC_BRIGHT_YELLOW)
WRAP(bright_blue, SSC_BRIGHT_BLUE)
WRAP(bright_magenta, SSC_BRIGHT_MAGENTA)
WRAP(bright_cyan, SSC_BRIGHT_CYAN)
WRAP(bright_white, SSC_BRIGHT_WHITE)

WRAP(bg_bright_black, SSC_BG_BRIGHT_BLACK)
WRAP(bg_bright_red, SSC_BG_BRIGHT_RED)
WRAP(bg_bright_green, SSC_BG_BRIGHT_GREEN)
WRAP(bg_bright_yellow, SSC_BG_BRIGHT_YELLOW)
WRAP(bg_bright_blue, SSC_BG_BRIGHT_BLUE)
WRAP(bg_bright_magenta, SSC_BG_BRIGHT_MAGENTA)
WRAP(bg_bright_cyan, SSC_BG_BRIGHT_CYAN)
WRAP(bg_bright_white, SSC_BG_BRIGHT_WHITE)

char* ssc_color_256(const char* t, int c) {
    char b[24]; snprintf(b,sizeof(b),"\033[38;5;%dm",c);
    return ssc_wrap(t,b);
}

char* ssc_bg_color_256(const char* t, int c) {
    char b[24]; snprintf(b,sizeof(b),"\033[48;5;%dm",c);
    return ssc_wrap(t,b);
}

char* ssc_color_rgb(const char* t, int r, int g, int b) {
    char buf[32]; snprintf(buf,sizeof(buf),"\033[38;2;%d;%d;%dm",r,g,b);
    return ssc_wrap(t,buf);
}

char* ssc_bg_color_rgb(const char* t, int r, int g, int b) {
    char buf[32]; snprintf(buf,sizeof(buf),"\033[48;2;%d;%d;%dm",r,g,b);
    return ssc_wrap(t,buf);
}

char* ssc_strip_ansi(const char* t) {
    if (!t) return NULL;
    int len = (int)strlen(t);
    char* r = (char*)malloc(len+1);
    if (!r) return NULL; int j=0;
    for (int i=0; t[i]; i++) {
        if (t[i] == '\x1b' || t[i] == 27) {
            i++; if (t[i]=='[') {
                i++; while (t[i] && ((t[i]>='0'&&t[i]<='9')||t[i]==';')) i++;
                if (t[i]=='m') continue; if (!t[i]) break;
            }
        }
        r[j++] = t[i];
    }
    r[j] = '\0'; return r;
}

void ssc_demo(void) {
    printf("\n=== ssetcolor v2.0 Demo ===\n\n");
    char* s;
    printf("Styles:\n  %s\n", ssc_bold("Bold"));
    s = ssc_italic("Italic"); printf("  %s\n",s); ssc_free(s);
    s = ssc_underline("Underline"); printf("  %s\n",s); ssc_free(s);
    s = ssc_reverse("Reverse"); printf("  %s\n",s); ssc_free(s);
    printf("\nForeground:\n  ");
    s = ssc_red("Red"); printf("%s ",s); ssc_free(s);
    s = ssc_green("Green"); printf("%s ",s); ssc_free(s);
    s = ssc_blue("Blue"); printf("%s\n",s); ssc_free(s);
    printf("  ");
    s = ssc_yellow("Yellow"); printf("%s ",s); ssc_free(s);
    s = ssc_cyan("Cyan"); printf("%s ",s); ssc_free(s);
    s = ssc_magenta("Magenta"); printf("%s\n",s); ssc_free(s);
    printf("\nBackground:\n  ");
    s = ssc_bg_red("Red BG"); printf("%s ",s); ssc_free(s);
    s = ssc_bg_green("Green BG"); printf("%s ",s); ssc_free(s);
    s = ssc_bg_blue("Blue BG"); printf("%s\n",s); ssc_free(s);
    printf("\n256-Color:\n  ");
    s = ssc_color_256("Orange(208)",208); printf("%s ",s); ssc_free(s);
    s = ssc_color_256("Purple(129)",129); printf("%s\n",s); ssc_free(s);
    printf("\nTrueColor:\n  ");
    s = ssc_color_rgb("CustomRGB",255,100,50); printf("%s\n",s); ssc_free(s);
    printf("\nComposed:\n  ");
    ssc_style_t* st = ssc_style_new();
    ssc_style_add(st,SSC_BOLD); ssc_style_add_fg(st,"red");
    s = ssc_style_apply(st,"Bold Red"); printf("%s\n",s); ssc_free(s);
    ssc_style_free(st);
    printf("\n=== End Demo ===\n\n");
}
