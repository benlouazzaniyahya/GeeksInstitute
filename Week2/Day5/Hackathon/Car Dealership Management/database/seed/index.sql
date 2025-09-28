
-- Create tables
CREATE TABLE IF NOT EXISTS salespeople (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vehicles (
    id SERIAL PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    type VARCHAR(20) NOT NULL,
    description TEXT,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    salesperson_id INTEGER NOT NULL REFERENCES salespeople(id) ON DELETE CASCADE,
    sale_date DATE NOT NULL,
    sale_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO salespeople (first_name, last_name, email, phone, hire_date) VALUES
('John', 'Doe', 'john.doe@dealership.com', '555-0101', '2020-01-15'),
('Jane', 'Smith', 'jane.smith@dealership.com', '555-0102', '2020-03-22'),
('Michael', 'Johnson', 'michael.j@dealership.com', '555-0103', '2019-11-05'),
('Sarah', 'Williams', 'sarah.w@dealership.com', '555-0104', '2021-02-10'),
('David', 'Brown', 'david.b@dealership.com', '555-0105', '2021-07-18'),
('Emily', 'Davis', 'emily.d@dealership.com', '555-0106', '2022-01-30'),
('James', 'Miller', 'james.m@dealership.com', '555-0107', '2022-04-12'),
('Lisa', 'Garcia', 'lisa.g@dealership.com', '555-0108', '2022-09-05'),
('Robert', 'Martinez', 'robert.m@dealership.com', '555-0109', '2023-02-20'),
('Jennifer', 'Anderson', 'jennifer.a@dealership.com', '555-0110', '2023-05-15');

INSERT INTO customers (first_name, last_name, email, phone, address) VALUES
('Michael', 'Wilson', 'm.wilson@email.com', '555-1001', '123 Main St, Anytown, USA'),
('Jessica', 'Taylor', 'j.taylor@email.com', '555-1002', '456 Oak Ave, Somewhere, USA'),
('David', 'Thomas', 'd.thomas@email.com', '555-1003', '789 Pine Rd, Nowhere, USA'),
('Sarah', 'Jackson', 's.jackson@email.com', '555-1004', '321 Elm St, Everywhere, USA'),
('James', 'White', 'j.white@email.com', '555-1005', '654 Maple Dr, Anywhere, USA'),
('Mary', 'Harris', 'm.harris@email.com', '555-1006', '987 Cedar Ln, Somewhere Else, USA'),
('Robert', 'Clark', 'r.clark@email.com', '555-1007', '147 Birch Blvd, Nowhere Else, USA'),
('Patricia', 'Lewis', 'p.lewis@email.com', '555-1008', '258 Spruce Way, Anywhere Else, USA'),
('Jennifer', 'Allen', 'j.allen@email.com', '555-1009', '369 Ash Ct, Everywhere Else, USA'),
('William', 'Young', 'w.young@email.com', '555-1010', '741 Fir Rd, Beyond Town, USA');

INSERT INTO vehicles (make, model, year, price, type, description, image_url) VALUES
('Toyota', 'Camry', 2023, 25199.00, 'sedan', 'Reliable and fuel-efficient sedan with advanced safety features.', 'https://example.com/toyota-camry.jpg'),
('Honda', 'CR-V', 2023, 28400.00, 'suv', 'Compact SUV with spacious interior and great fuel economy.', 'https://example.com/honda-crv.jpg'),
('Ford', 'F-150', 2023, 36470.00, 'truck', 'Best-selling truck with impressive towing capacity and power.', 'https://example.com/ford-f150.jpg'),
('Tesla', 'Model 3', 2023, 38990.00, 'sedan', 'Electric sedan with autopilot and long range capability.', 'https://example.com/tesla-model3.jpg'),
('Chevrolet', 'Silverado', 2023, 37600.00, 'truck', 'Durable truck with multiple engine options and tech features.', 'https://example.com/chevy-silverado.jpg'),
('BMW', 'X5', 2023, 62300.00, 'suv', 'Luxury SUV with premium interior and powerful performance.', 'https://example.com/bmw-x5.jpg'),
('Mercedes-Benz', 'C-Class', 2023, 43250.00, 'sedan', 'Luxury sedan with cutting-edge technology and comfort.', 'https://example.com/mercedes-c.jpg'),
('Audi', 'Q7', 2023, 55800.00, 'suv', 'Premium SUV with Quattro all-wheel drive and spacious cabin.', 'https://example.com/audi-q7.jpg'),
('Nissan', 'Rogue', 2023, 28290.00, 'suv', 'Compact SUV with available hybrid technology and cargo space.', 'https://example.com/nissan-rogue.jpg'),
('Hyundai', 'Elantra', 2023, 21250.00, 'sedan', 'Stylish sedan with advanced safety features and great warranty.', 'https://example.com/hyundai-elantra.jpg'),
('Jeep', 'Wrangler', 2023, 31900.00, 'suv', 'Iconic off-road vehicle with removable doors and roof.', 'https://example.com/jeep-wrangler.jpg'),
('Subaru', 'Outback', 2023, 29145.00, 'suv', 'Versatile wagon with standard all-wheel drive and cargo space.', 'https://example.com/subaru-outback.jpg'),
('Lexus', 'RX', 2023, 47350.00, 'suv', 'Luxury SUV with premium comfort and advanced safety.', 'https://example.com/lexus-rx.jpg'),
('Mazda', 'CX-5', 2023, 28450.00, 'suv', 'Compact SUV with upscale interior and responsive handling.', 'https://example.com/mazda-cx5.jpg'),
('Volkswagen', 'Tiguan', 2023, 26495.00, 'suv', 'Compact SUV with turbocharged engine and versatile seating.', 'https://example.com/vw-tiguan.jpg');

INSERT INTO sales (vehicle_id, customer_id, salesperson_id, sale_date, sale_price) VALUES
(1, 1, 1, '2023-01-15', 24500.00),
(2, 2, 2, '2023-02-20', 27800.00),
(3, 3, 3, '2023-03-10', 35500.00),
(4, 4, 4, '2023-04-05', 38200.00),
(5, 5, 5, '2023-05-12', 36900.00),
(6, 6, 6, '2023-06-18', 60500.00),
(7, 7, 7, '2023-07-22', 42100.00),
(8, 8, 8, '2023-08-30', 54300.00),
(9, 9, 9, '2023-09-14', 27500.00),
(10, 10, 10, '2023-10-05', 20800.00),
(11, 1, 1, '2023-11-19', 31200.00),
(12, 2, 2, '2023-12-23', 28500.00),
(13, 3, 3, '2023-01-05', 46200.00),
(14, 4, 4, '2023-02-15', 27800.00),
(15, 5, 5, '2023-03-25', 25900.00);
