cmake_minimum_required(VERSION 3.8)
project(more_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/AddressBook.msg"
)

install(PROGRAMS scripts/publish_address_book.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME publish_address_book
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
