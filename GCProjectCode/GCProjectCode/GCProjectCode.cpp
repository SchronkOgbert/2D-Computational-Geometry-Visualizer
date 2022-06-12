#include <iostream>
#include <boost/asio.hpp>
#include <boost/numeric/ublas/vector.hpp>

int main()
{
    boost::asio::io_context io;
    boost::numeric::ublas::vector<int> v(3);
    v[0] = 9;
    v.resize(10);
    std::cout << v[0] << '\n';
    std::cout << v.size() << '\n';
    v.insert_element(3, 23);
    std::cout << v.size() << '\n';

    auto timer = boost::asio::steady_timer(io,
        boost::asio::chrono::seconds(1));

    std::cout << "Start\n";
    io.run();
    timer.wait();
    std::cout << "Stop\n";
}