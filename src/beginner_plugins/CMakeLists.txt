cmake_minimum_required(VERSION 3.8)
project(beginner_plugins)

find_package(ament_cmake REQUIRED)
find_package(pluginlib REQUIRED)

add_library(beginner_polygons SHARED src/polygons.cpp)
target_compile_features(beginner_polygons PUBLIC cxx_std_17)
target_include_directories(beginner_polygons PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
target_link_libraries(beginner_polygons PUBLIC pluginlib::pluginlib)
pluginlib_export_plugin_description_file(beginner_plugins plugins.xml)

add_executable(area_demo src/area_demo.cpp)
target_compile_features(area_demo PUBLIC cxx_std_17)
target_include_directories(area_demo PRIVATE include)
target_link_libraries(area_demo PRIVATE pluginlib::pluginlib)
install(TARGETS beginner_polygons
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)
install(TARGETS area_demo DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY include/ DESTINATION include)
ament_export_include_directories(include)
ament_export_dependencies(pluginlib)
ament_package()
