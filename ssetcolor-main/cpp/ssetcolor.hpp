#ifndef SSETCOLOR_HPP
#define SSETCOLOR_HPP

#include <string>
#include <ostream>
#include "ssetcolor.h"

namespace ssetcolor {

inline std::string wrap(const std::string& text, const char* ansi_code) {
    if (ansi_code) {
        return ansi_code + text + "\033[0m";
    }
    return text;
}

// Style builder class
class style {
public:
    style() : m_style(ssc_style_new()) {}
    ~style() { ssc_style_free(m_style); }

    style& add(const char* code) { ssc_style_add(m_style, code); return *this; }

    style& bold()       { return add(SSC_BOLD); }
    style& italic()     { return add(SSC_ITALIC); }
    style& underline()  { return add(SSC_UNDERLINE); }
    style& reverse()    { return add(SSC_REVERSE); }
    style& fade()       { return add(SSC_FADE); }
    style& blink()      { return add(SSC_BLINK_SLOW); }
    style& hidden()     { return add(SSC_HIDDEN); }

    style& fg(const char* color) { ssc_style_add_fg(m_style, color); return *this; }
    style& bg(const char* color) { ssc_style_add_bg(m_style, color); return *this; }
    style& fg256(int c) { ssc_style_add_fg_256(m_style, c); return *this; }
    style& bg256(int c) { ssc_style_add_bg_256(m_style, c); return *this; }
    style& fgrgb(int r, int g, int b) { ssc_style_add_fg_rgb(m_style, r, g, b); return *this; }
    style& bgrgb(int r, int g, int b) { ssc_style_add_bg_rgb(m_style, r, g, b); return *this; }

    std::string apply(const std::string& text) const {
        char* r = ssc_style_apply(m_style, text.c_str());
        if (!r) return text;
        std::string result(r);
        ssc_free(r);
        return result;
    }

private:
    ssc_style_t* m_style;
};

// Foreground colors
inline std::string bold(const std::string& t)       { char* r = ssc_bold(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string italic(const std::string& t)     { char* r = ssc_italic(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string underline(const std::string& t)  { char* r = ssc_underline(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string reverse(const std::string& t)    { char* r = ssc_reverse(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string fade(const std::string& t)       { char* r = ssc_fade(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string blink(const std::string& t)      { char* r = ssc_blink_slow(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string hidden(const std::string& t)     { char* r = ssc_hidden(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }

inline std::string black(const std::string& t)      { char* r = ssc_black(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string red(const std::string& t)        { char* r = ssc_red(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string green(const std::string& t)      { char* r = ssc_green(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string yellow(const std::string& t)     { char* r = ssc_yellow(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string blue(const std::string& t)       { char* r = ssc_blue(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string magenta(const std::string& t)    { char* r = ssc_magenta(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string cyan(const std::string& t)       { char* r = ssc_cyan(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string white(const std::string& t)      { char* r = ssc_white(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }

// Background colors
inline std::string bg_black(const std::string& t)   { char* r = ssc_bg_black(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string bg_red(const std::string& t)     { char* r = ssc_bg_red(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string bg_green(const std::string& t)   { char* r = ssc_bg_green(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string bg_yellow(const std::string& t)  { char* r = ssc_bg_yellow(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string bg_blue(const std::string& t)    { char* r = ssc_bg_blue(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string bg_magenta(const std::string& t) { char* r = ssc_bg_magenta(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string bg_cyan(const std::string& t)    { char* r = ssc_bg_cyan(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }
inline std::string bg_white(const std::string& t)   { char* r = ssc_bg_white(t.c_str()); std::string s(r?r:t); ssc_free(r); return s; }

// Stream manipulator helper
class stream_style {
public:
    stream_style(const char* code) : m_code(code) {}
    const char* code() const { return m_code; }
private:
    const char* m_code;
};

inline std::ostream& operator<<(std::ostream& os, const stream_style& s) {
    os << s.code();
    return os;
}

inline std::ostream& operator<<(std::ostream& os, const style& s) {
    // Just for applying to next string - not fully implemented for streaming
    return os;
}

// Stream manipulator constants
inline const stream_style reset()       { return stream_style(SSC_RESET); }
inline const stream_style stream_bold() { return stream_style(SSC_BOLD); }
inline const stream_style stream_red()  { return stream_style(SSC_RED); }
inline const stream_style stream_blue() { return stream_style(SSC_BLUE); }

} // namespace ssetcolor

#endif // SSETCOLOR_HPP
