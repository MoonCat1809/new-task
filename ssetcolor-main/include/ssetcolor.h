#ifndef SSETCOLOR_H
#define SSETCOLOR_H

#ifdef __cplusplus
extern "C" {
#endif

/* === Export/Import macros for shared library === */
#if defined(_WIN32) || defined(_WIN64)
#  if defined(SSETCOLOR_BUILD_SHARED)
#    define SSC_API __declspec(dllexport)
#  else
#    define SSC_API __declspec(dllimport)
#  endif
#else
#  define SSC_API __attribute__((visibility("default")))
#endif

/* === Terminal capability detection === */
SSC_API int ssc_supports_color(void);
SSC_API int ssc_color_depth(void);

/* === ANSI escape code constants === */
#define SSC_RESET         "\033[0m"
#define SSC_BOLD          "\033[1m"
#define SSC_FADE          "\033[2m"
#define SSC_ITALIC        "\033[3m"
#define SSC_UNDERLINE     "\033[4m"
#define SSC_BLINK_SLOW    "\033[5m"
#define SSC_BLINK_FAST    "\033[6m"
#define SSC_REVERSE       "\033[7m"
#define SSC_HIDDEN        "\033[8m"
#define SSC_CONCEALED     "\033[9m"
#define SSC_BOLD_OFF      "\033[21m"
#define SSC_ITALIC_OFF    "\033[23m"
#define SSC_UNDERLINE_OFF "\033[24m"
#define SSC_BLINK_OFF     "\033[25m"
#define SSC_REVERSE_OFF   "\033[27m"
#define SSC_HIDDEN_OFF    "\033[28m"

/* Standard foreground colors */
#define SSC_BLACK   "\033[30m"
#define SSC_RED     "\033[31m"
#define SSC_GREEN   "\033[32m"
#define SSC_YELLOW  "\033[33m"
#define SSC_BLUE    "\033[34m"
#define SSC_MAGENTA "\033[35m"
#define SSC_CYAN    "\033[36m"
#define SSC_WHITE   "\033[37m"

/* Bright foreground colors */
#define SSC_BRIGHT_BLACK   "\033[90m"
#define SSC_BRIGHT_RED     "\033[91m"
#define SSC_BRIGHT_GREEN   "\033[92m"
#define SSC_BRIGHT_YELLOW  "\033[93m"
#define SSC_BRIGHT_BLUE    "\033[94m"
#define SSC_BRIGHT_MAGENTA "\033[95m"
#define SSC_BRIGHT_CYAN    "\033[96m"
#define SSC_BRIGHT_WHITE   "\033[97m"

/* Standard background colors */
#define SSC_BG_BLACK   "\033[40m"
#define SSC_BG_RED     "\033[41m"
#define SSC_BG_GREEN   "\033[42m"
#define SSC_BG_YELLOW  "\033[43m"
#define SSC_BG_BLUE    "\033[44m"
#define SSC_BG_MAGENTA "\033[45m"
#define SSC_BG_CYAN    "\033[46m"
#define SSC_BG_WHITE   "\033[47m"

/* Bright background colors */
#define SSC_BG_BRIGHT_BLACK   "\033[100m"
#define SSC_BG_BRIGHT_RED     "\033[101m"
#define SSC_BG_BRIGHT_GREEN   "\033[102m"
#define SSC_BG_BRIGHT_YELLOW  "\033[103m"
#define SSC_BG_BRIGHT_BLUE    "\033[104m"
#define SSC_BG_BRIGHT_MAGENTA "\033[105m"
#define SSC_BG_BRIGHT_CYAN    "\033[106m"
#define SSC_BG_BRIGHT_WHITE   "\033[107m"

/* === Style builder (composable) === */
typedef struct ssc_style ssc_style_t;

SSC_API ssc_style_t* ssc_style_new(void);
SSC_API void ssc_style_free(ssc_style_t* style);
SSC_API void ssc_style_add(ssc_style_t* style, const char* ansi_code);
SSC_API void ssc_style_add_fg(ssc_style_t* style, const char* color_name);
SSC_API void ssc_style_add_bg(ssc_style_t* style, const char* color_name);
SSC_API void ssc_style_add_fg_256(ssc_style_t* style, int color_code);
SSC_API void ssc_style_add_bg_256(ssc_style_t* style, int color_code);
SSC_API void ssc_style_add_fg_rgb(ssc_style_t* style, int r, int g, int b);
SSC_API void ssc_style_add_bg_rgb(ssc_style_t* style, int r, int g, int b);

SSC_API int ssc_style_apply_buf(char* buf, int buf_size, const ssc_style_t* style, const char* text);
SSC_API char* ssc_style_apply(const ssc_style_t* style, const char* text);

SSC_API int ssc_wrap_buf(char* buf, int buf_size, const char* text, const char* ansi_code);
SSC_API char* ssc_wrap(const char* text, const char* ansi_code);

/* === Pre-built convenience functions === */
SSC_API char* ssc_bold(const char* text);
SSC_API char* ssc_fade(const char* text);
SSC_API char* ssc_italic(const char* text);
SSC_API char* ssc_underline(const char* text);
SSC_API char* ssc_blink_slow(const char* text);
SSC_API char* ssc_blink_fast(const char* text);
SSC_API char* ssc_reverse(const char* text);
SSC_API char* ssc_hidden(const char* text);
SSC_API char* ssc_concealed(const char* text);

SSC_API char* ssc_black(const char* text);
SSC_API char* ssc_red(const char* text);
SSC_API char* ssc_green(const char* text);
SSC_API char* ssc_yellow(const char* text);
SSC_API char* ssc_blue(const char* text);
SSC_API char* ssc_magenta(const char* text);
SSC_API char* ssc_cyan(const char* text);
SSC_API char* ssc_white(const char* text);

SSC_API char* ssc_bg_black(const char* text);
SSC_API char* ssc_bg_red(const char* text);
SSC_API char* ssc_bg_green(const char* text);
SSC_API char* ssc_bg_yellow(const char* text);
SSC_API char* ssc_bg_blue(const char* text);
SSC_API char* ssc_bg_magenta(const char* text);
SSC_API char* ssc_bg_cyan(const char* text);
SSC_API char* ssc_bg_white(const char* text);

SSC_API char* ssc_bright_black(const char* text);
SSC_API char* ssc_bright_red(const char* text);
SSC_API char* ssc_bright_green(const char* text);
SSC_API char* ssc_bright_yellow(const char* text);
SSC_API char* ssc_bright_blue(const char* text);
SSC_API char* ssc_bright_magenta(const char* text);
SSC_API char* ssc_bright_cyan(const char* text);
SSC_API char* ssc_bright_white(const char* text);

SSC_API char* ssc_bg_bright_black(const char* text);
SSC_API char* ssc_bg_bright_red(const char* text);
SSC_API char* ssc_bg_bright_green(const char* text);
SSC_API char* ssc_bg_bright_yellow(const char* text);
SSC_API char* ssc_bg_bright_blue(const char* text);
SSC_API char* ssc_bg_bright_magenta(const char* text);
SSC_API char* ssc_bg_bright_cyan(const char* text);
SSC_API char* ssc_bg_bright_white(const char* text);

SSC_API char* ssc_color_256(const char* text, int color_code);
SSC_API char* ssc_bg_color_256(const char* text, int color_code);
SSC_API char* ssc_color_rgb(const char* text, int r, int g, int b);
SSC_API char* ssc_bg_color_rgb(const char* text, int r, int g, int b);

SSC_API void ssc_free(char* ptr);
SSC_API void ssc_demo(void);
SSC_API char* ssc_strip_ansi(const char* text);

#ifdef __cplusplus
}
#endif

#endif /* SSETCOLOR_H */
