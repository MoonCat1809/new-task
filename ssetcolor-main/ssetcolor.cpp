#include <string>
#include <iostream>

namespace ssetcolor
{
    std::string reset(const std::string& text) { return "\033[0m" + text + "\033[0m"; }
    std::string bold(const std::string& text) { return "\033[1m" + text + "\033[0m"; }
    std::string fade(const std::string& text) { return "\033[2m" + text + "\033[0m"; }
    std::string italic(const std::string& text) { return "\033[3m" + text + "\033[0m"; }
    std::string underline(const std::string& text) { return "\033[4m" + text + "\033[0m"; }
    std::string blink_slow(const std::string& text) { return "\033[5m" + text + "\033[0m"; }
    std::string blink_fast(const std::string& text) { return "\033[6m" + text + "\033[0m"; }
    std::string reverse(const std::string& text) { return "\033[7m" + text + "\033[0m"; }
    std::string hidden(const std::string& text) { return "\033[8m" + text + "\033[0m"; }
    std::string concealed(const std::string& text) { return "\033[9m" + text + "\033[0m"; }
    std::string blink_off(const std::string& text) { return "\033[25m" + text + "\033[0m"; }
    std::string conceal_off(const std::string& text) { return "\033[28m" + text + "\033[0m"; }

    std::string black(const std::string& text) { return "\033[30m" + text + "\033[0m"; }
    std::string red(const std::string& text) { return "\033[31m" + text + "\033[0m"; }
    std::string green(const std::string& text) { return "\033[32m" + text + "\033[0m"; }
    std::string yellow(const std::string& text) { return "\033[33m" + text + "\033[0m"; }
    std::string blue(const std::string& text) { return "\033[34m" + text + "\033[0m"; }
    std::string magenta(const std::string& text) { return "\033[35m" + text + "\033[0m"; }
    std::string cyan(const std::string& text) { return "\033[36m" + text + "\033[0m"; }
    std::string white(const std::string& text) { return "\033[37m" + text + "\033[0m"; }

    std::string orange(const std::string& text) { return "\033[38;5;208m" + text + "\033[0m"; }
    std::string purple(const std::string& text) { return "\033[38;5;129m" + text + "\033[0m"; }

    void demo() {
        std::cout << red("Hello, ") << green("World!") << std::endl;
        std::cout << bold("This is bold text.") << std::endl;
        std::cout << fade("This is faded text.") << std::endl;
        std::cout << italic("This is italic text.") << std::endl;
        std::cout << underline("This is underlined text.") << std::endl;
        std::cout << blink_slow("This text is blinking slowly.") << std::endl;
        std::cout << blink_fast("This text is blinking fast.") << std::endl;
        std::cout << reverse("This text is reversed.") << std::endl;
        std::cout << hidden("This text is hidden.") << std::endl;
        std::cout << concealed("This text is concealed.") << std::endl;
        std::cout << blink_off("This text is no longer blinking.") << std::endl;
        std::cout << conceal_off("This text is no longer concealed.") << std::endl;
    }
}