# File: python/file_handler.py
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
write_to_file("greeting.txt", "Hello from a Python snippet!")