#include <cmath>
#include "beginner_plugins/polygon.hpp"
#include "pluginlib/class_list_macros.hpp"

namespace beginner_plugins
{
class Square : public Polygon
{
public:
  void initialize(double side) override {side_ = side;}
  double area() const override {return side_ * side_;}

private:
  double side_ = 0.0;
};

class Triangle : public Polygon
{
public:
  void initialize(double side) override {side_ = side;}
  double area() const override {return std::sqrt(3.0) * side_ * side_ / 4.0;}

private:
  double side_ = 0.0;
};
}  // namespace beginner_plugins

PLUGINLIB_EXPORT_CLASS(beginner_plugins::Square, beginner_plugins::Polygon)
PLUGINLIB_EXPORT_CLASS(beginner_plugins::Triangle, beginner_plugins::Polygon)
