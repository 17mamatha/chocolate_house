This is a Python-based application for managing a fictional chocolate house's offerings, including seasonal flavors, ingredient inventory, and customer flavor suggestions with allergy concerns. The application uses SQLite for database management and is containerized with Docker.
1.Clone the repository:
git clone https://github.com/your-username/chocolate_house_app.git
2.Navigate to the project directory:
cd chocolate_house_app
3.Install dependencies:
pip install -r requirements.txt
4.Initialize the database: 
python -c "from database import initialize_db; initialize_db()"
Run the application with the following command:
python app.py
Docker Commands
1.Build the Docker image:
docker build -t chocolate_house_app .
2.Run the Docker container:
docker run -it chocolate_house_app
