# Q1 Task 1

restaurant_menu = {
    "Starters": {"Soup": 5.99},  # Bruschetta removed
    "Main Course": {"Steak": 17.99, "Salmon": 13.99},  # Steak price updated
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99},
    "Beverages": {"Coffee": 2.50, "Soda": 1.99},  # New category with drinks
}

# Q Task 1

def book_room(hotel_rooms, room_number, customer_name):
  """Books a room and assigns it to a customer.

  Args:
    hotel_rooms: A dictionary containing room information.
    room_number: The room number to be booked (as a string).
    customer_name: The name of the customer booking the room.

  Returns:
    A message indicating success or failure.
  """
  if room_number in hotel_rooms:
    if hotel_rooms[room_number]["status"] == "available":
      hotel_rooms[room_number]["status"] = "booked"
      hotel_rooms[room_number]["customer"] = customer_name
      return f"Room {room_number} booked for {customer_name}"
    else:
      return f"Room {room_number} is already occupied."
  else:
    return f"Room {room_number} does not exist."

def check_out(hotel_rooms, room_number):
  """Checks out a customer from a room.

  Args:
    hotel_rooms: A dictionary containing room information.
    room_number: The room number of the customer checking out (as a string).

  Returns:
    A message indicating success or failure.
  """
  if room_number in hotel_rooms:
    if hotel_rooms[room_number]["status"] == "booked":
      hotel_rooms[room_number]["status"] = "available"
      hotel_rooms[room_number]["customer"] = ""
      return f"Customer has checked out of room {room_number}"
    else:
      return f"Room {room_number} is already available."
  else:
    return f"Room {room_number} does not exist."

def display_room_status(hotel_rooms):
  """Displays the status of all rooms in the hotel.

  Args:
    hotel_rooms: A dictionary containing room information.
  """
  print("Room Status:")
  for room_number, room_info in hotel_rooms.items():
    status = room_info["status"]
    customer = room_info["customer"] if room_info["customer"] else "None"
    print(f"Room {room_number}: {status} - Occupied by: {customer}")

# Example usage
hotel_rooms = {
  "101": {"status": "available", "customer": ""},
  "102": {"status": "booked", "customer": "John Doe"}
}

print(book_room(hotel_rooms, "103", "Jane Smith"))  # Book room 103 for Jane Smith
display_room_status(hotel_rooms)  # Display room status

print(check_out(hotel_rooms, "102"))  # John Doe checks out of room 102
display_room_status(hotel_rooms)  # Display room status

# Q1 Task1

def generate_ticket_id():
  """Generates a unique ticket ID string."""
  # Implement logic to generate a unique ID (e.g., using a counter or random string)
  # For simplicity, we'll use a counter here
  global ticket_counter
  ticket_counter += 1
  return f"Ticket{ticket_counter:03d}"  # Format to 3-digit string

def open_ticket(service_tickets, customer_name, issue_description):
  """Opens a new customer service ticket.

  Args:
    service_tickets: A dictionary containing ticket information.
    customer_name: The name of the customer submitting the ticket.
    issue_description: A description of the customer's issue.

  Returns:
    The newly generated ticket ID.
  """
  ticket_id = generate_ticket_id()
  service_tickets[ticket_id] = {
      "Customer": customer_name,
      "Issue": issue_description,
      "Status": "open"
  }
  return ticket_id

def update_ticket_status(service_tickets, ticket_id, new_status):
  """Updates the status of an existing ticket.

  Args:
    service_tickets: A dictionary containing ticket information.
    ticket_id: The ID of the ticket to update.
    new_status: The new status for the ticket ("open" or "closed").

  Returns:
    A message indicating success or failure.
  """
  if ticket_id in service_tickets:
    if new_status in ("open", "closed"):
      service_tickets[ticket_id]["Status"] = new_status
      return f"Ticket {ticket_id} status updated to {new_status}"
    else:
      return "Invalid status. Please use 'open' or 'closed'."
  else:
    return f"Ticket {ticket_id} not found."

def display_tickets(service_tickets, status=None):
  """Displays all tickets or filters by status.

  Args:
    service_tickets: A dictionary containing ticket information.
    status (optional): The status to filter by ("open" or "closed").
  """
  print("Customer Service Tickets:")
  if status:
    print(f"  Filtering by status: {status}")
  for ticket_id, ticket_info in service_tickets.items():
    if not status or ticket_info["Status"] == status:
      print(f"  Ticket ID: {ticket_id}")
      print(f"    Customer: {ticket_info['Customer']}")
      print(f"    Issue: {ticket_info['Issue']}")
      print(f"    Status: {ticket_info['Status']}")
      print("")

# Initialize with some sample tickets and ticket counter
ticket_counter = 0  # Global variable for unique ticket ID generation
service_tickets = {
  "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
  "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Example usage
new_ticket_id = open_ticket(service_tickets, "Charlie", "Slow loading website")
print(f"Ticket opened with ID: {new_ticket_id}")

update_ticket_status(service_tickets, "Ticket001", "closed")
display_tickets(service_tickets)  # Display all tickets

display_tickets(service_tickets, "open")  # Filter and display open tickets


# Q4 task1

import copy

def update_sales_data(sales_data, week_number, category, new_sales_figure):
  """
  Creates a deep copy of sales data and updates a specific sales figure.

  Args:
    sales_data: A dictionary containing weekly sales data.
    week_number: The week number to update (as a string).
    category: The product category to update (e.g., "Electronics").
    new_sales_figure: The new sales figure for the specified category.

  Returns:
    A deep copy of the sales data with the updated sales figure.
  """
  copied_data = copy.deepcopy(sales_data)  # Deep copy to modify without affecting original
  if week_number in copied_data:
    if category in copied_data[week_number]:
      copied_data[week_number][category] = new_sales_figure
      return f"Sales figure for '{category}' in 'Week {week_number}' updated to {new_sales_figure}."
    else:
      return f"Category '{category}' not found in 'Week {week_number}'"
  else:
    return f"Week {week_number} not found in sales data."

# Example usage
weekly_sales = {
  "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
  "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copied_sales_data = update_sales_data(weekly_sales, "Week 2", "Electronics", 18000)
print(copied_sales_data)  # Print the update message

print(weekly_sales)  # Original data remains unchanged
