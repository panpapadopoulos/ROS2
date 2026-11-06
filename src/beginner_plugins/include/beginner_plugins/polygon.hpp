#ifndef BEGINNER_PLUGINS__POLYGON_HPP_
#define BEGINNER_PLUGINS__POLYGON_HPP_

namespace beginner_plugins
{
class Polygon
{
public:
  virtual ~Polygon() = default;
  virtual void initialize(double side) = 0;
  virtual double area() const = 0;
};
}  // namespace beginner_plugins

#endif  // BEGINNER_PLUGINS__POLYGON_HPP_
