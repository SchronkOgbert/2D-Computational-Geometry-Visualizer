#include <iostream>
#include <boost/asio.hpp>

int main()
{
    boost::asio::io_context io;

    auto timer = boost::asio::steady_timer(io,
        boost::asio::chrono::seconds(1));

    std::cout << "Start\n";
    io.run();
    timer.wait();
    std::cout << "Stop\n";
}