def submit_data(data, client, address):
    # Convert the data to bytes
    data_bytes = data.encode('utf-8')

    # Connect to the server at the given address
    client.connect(address)

    # Send the data to the server
    client.send(data_bytes)

    # Close the connection
    client.close()
