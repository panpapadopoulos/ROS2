#include <iomanip>
#include <iostream>
#include <string>
#include "beginner_plugins/polygon.hpp"
#include "pluginlib/class_loader.hpp"

int main()
{
  try {
    pluginlib::ClassLoader<beginner_plugins::Polygon> loader(
      "beginner_plugins", "beginner_plugins::Polygon");
    for (const std::string name : {"Square", "Triangle"}) {
      auto polygon = loader.createSharedInstance("beginner_plugins::" + name);
      polygon->initialize(10.0);
      std::cout << name << " area: " << std::fixed << std::setprecision(2)
                << polygon->area() << '\n';
    }
  } catch (const pluginlib::PluginlibException & error) {
    std::cerr << "Plugin loading failed: " << error.what() << '\n';
    return 1;
  }
  return 0;
}
