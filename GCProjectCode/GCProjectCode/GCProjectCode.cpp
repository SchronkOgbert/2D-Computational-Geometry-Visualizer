#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/convex_hull_2.h>
#include <CGAL/Convex_hull_traits_adapter_2.h>
#include <CGAL/property_map.h>
#include <CGAL/Point_2.h>
#include <vector>
#include <numeric>
#include <exception>
#include <string>


// simplyfying the syntax so we don't have to call a million namespaces
typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef K::Point_2 Point_2;
typedef CGAL::Convex_hull_traits_adapter_2<K,
    CGAL::Pointer_property_map<Point_2>::type > Convex_hull_traits_2;

/**
 * \brief converts a c string to std::string
 * \param a c string to be converted
 * \return the std::string
 */
std::string convertToString(char* a)
{
    std::string s;
    for (int i = 0; i < strlen(a); i++) 
    {
        s += a[i];
    }
    return s;
}


/**
 * \brief moves the coordinates received through the cl into a vector of Point_2
 * \param argc number of arguments from the command line
 * \param argv values as c strings
 * \return a vector with the Point_2 elements
 */
std::vector<Point_2> getCommandLinePoints(int argc, char* argv[])
{
    std::vector<Point_2> results;
    // counting starts from 1 since argv[0] is the program itself
    // increments by 2 steps because each 2 values represent the coords of a single point
    // from the command line validation function it is guaranteed it can't go out of range
    for(int i = 1; i < argc; i += 2)
    {
        try
        {
            results.emplace_back
            (
                std::stoi(argv[i]),
                std::stoi(argv[i + 1])
            );
        }
        catch (std::exception& e)
        {
            // if one of the values cannot be converted to a number abort the program
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
        // there is always at least one argument, the program itself
        // if that's the only one we can't calculate a hull
        throw std::exception("No points given");
	}
    if(argc % 2 == 0)
    {
        // we need an even number of coords to get any number of points
        // therefore we should have an odd number of command line arguments,
        // including the default argument which is the program
		throw std::exception("Coordinates must be an even number");
    }
}

int main(int argc, char* argv[])
{
	try
	{
		validateCommandLine(argc);		
	}
	catch (std::exception& e)
	{
        std::cout << e.what() << '\n';
        exit(1);
	}

    // we need to parse the command line arguments and have an array for the results
    auto points = getCommandLinePoints(argc, argv);
    // the reason a classic array was used instead of a container is that
    // the geogebra function expects a classic array for the results
    const auto result = new Point_2[argc];

    // calculate the points on the hull with the geogebra function
    const Point_2* ptr = CGAL::convex_hull_2
	(
        points.begin(), 
        points.end(), 
        result
    );

    // print the resulting points, one on each line
    for (int i = 0; i < ptr - result; i++)
    {
        std::cout << result[i] << '\n';
    }

    // free dynamic array
    delete[] result;
    return 0;
}