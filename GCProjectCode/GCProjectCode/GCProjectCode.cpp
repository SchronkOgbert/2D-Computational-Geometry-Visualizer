#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/convex_hull_2.h>
#include <CGAL/Convex_hull_traits_adapter_2.h>
#include <CGAL/property_map.h>
#include <CGAL/Point_2.h>
#include <vector>
#include <numeric>
#include <exception>
#include <string>

typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef K::Point_2 Point_2;
typedef CGAL::Convex_hull_traits_adapter_2<K,
    CGAL::Pointer_property_map<Point_2>::type > Convex_hull_traits_2;

std::string convertToString(char* a)
{
    std::string s;
    for (int i = 0; i < strlen(a); i++) 
    {
        s += a[i];
    }
    return s;
}


std::vector<Point_2> getCommandLinePoints(int argc, char* argv[])
{
    std::vector<Point_2> results;
    int buffer;
    for(int i = 1; i < argc; i++)
    {
        try
        {
	        if(i % 2)
	        {
	            buffer = std::stoi(argv[i]);
	            continue;
	        }
            results.emplace_back
            (
                buffer,
                std::stoi(argv[i])
            );
        }
        catch (std::exception& e)
        {
            std::cout << e.what() << '\n';
            exit(3);
        }
    }
    return results;
}

void validateCommandLine(int argc)
{
	if(argc == 1)
	{
        std::cout << "No points given\n";
        exit(1);
	}
    if(argc % 2 == 0)
    {
        std::cout << "Coordinates must be an even number\n";
        exit(2);
    }
}

int main(int argc, char* argv[])
{
    validateCommandLine(argc);
    auto points = getCommandLinePoints(argc, argv);
    auto result = new Point_2[argc];
    const Point_2* ptr = CGAL::convex_hull_2
	(
        points.begin(), 
        points.end(), 
        result
    );
    //std::cout << ptr - result << " points on the convex hull:" << std::endl;
    for (int i = 0; i < ptr - result; i++)
    {
        std::cout << result[i] << std::endl;
    }
    delete[] result;

    /*auto points = getCommandLinePoints(argc, argv);
    std::vector<std::size_t> indices(points.size()), out;
    std::iota(indices.begin(), indices.end(), 0);
    CGAL::convex_hull_2
		(
            indices.begin(), 
            indices.end(), 
	        std::back_inserter(out),
	        CGAL::Convex_hull_traits_2(CGAL::make_property_map(points))
        );
    for (const std::size_t i : out) 
    {
        std::cout << "points[" << i << "] = " << points[i] << std::endl;
    }*/
    //system("pause");
    return 0;
}