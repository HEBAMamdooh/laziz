# Laziz: Smart Recipe Assistant, Your life with a healthy flavour

## Project Overview

Laziz is an interactive web application designed to help users track their Meals and receive personalized diet plans and health advice based on their inputs and goals. The app incorporates machine learning to improve suggestions over time based on user feedback and progress.

## Key Features

- **Meal Planning and Nutrition Tracking:** Users can create and manage meal plans and track their nutritional intake.
- **Integration with Fitness Trackers:** Connects with third-party fitness trackers to monitor physical activity.
- **AI-based Health Suggestions:** Provides personalized health improvement suggestions.
- **Community Features:** Allows users to connect with others for motivation and support.

## Team

- **Heba** - Backend Developer and Database Manager
  - Role: Responsible for setting up and maintaining the backend infrastructure and managing the database.

## Technologies

- **Backend:** Python - Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript, Tailwind (UI Framework)
- **AI/ML:** TensorFlow or scikit-learn
- **Version Control:** Git, GitHub
- **API Integration:** Fitbit API (for fitness tracking data)

## Challenge Statement

- **Problem to Solve:** Laziz aims to provide a comprehensive platform for users to track their health metrics and receive personalized advice to improve their health and fitness.
- **Scope Limitation:** The app will not provide medical diagnoses or treatment plans. It is intended to offer general health and diet advice.
- **Target Users:** Individuals looking to improve their health and fitness through better diet and exercise habits.
- **Locale:** The project is not dependent on a specific locale and can be used globally.

## Risks

- **Technical Risks:**
  - **AI Integration Complexity:** Ensuring the AI suggestions are accurate and personalized.
    - _Mitigation:_ Start with a simple recommendation system and gradually enhance it.
  - **API Integration:** Issues with integrating third-party APIs.
    - _Mitigation:_ Thoroughly test API integration and have fallback options.
- **Non-Technical Risks:**
  - **User Adoption:** Difficulty in getting users to adopt and consistently use the app.
    - _Mitigation:_ Focus on user-friendly design and engaging features.

## Infrastructure

- **Branching and Merging:** GitHub Flow - feature branches are created for each new feature or fix, and merged into the main branch after review.
- **Data Population:** Initial data populated through user inputs and integrations with third-party APIs.

## Existing Solutions

- **MyFitnessPal:** Similar features for meal tracking but lacks AI-based personalized suggestions.
- **Fitbit:** Great for tracking fitness activities but does not provide comprehensive meal planning and health advice.
- **Noom:** Provides personalized health plans but is primarily focused on weight loss.

## APIs and Methods

- **/api/auth**
  - `POST /login`: Authenticates user and returns session token.
  - `POST /register`: Registers a new user.
- **/api/user**
  - `GET /profile`: Returns the user's profile information.
  - `PUT /profile`: Updates the user's profile information.
- **/api/health-data**
  - `GET /`: Retrieves user's health data.
  - `POST /`: Submits new health data.
- **/api/meal-plans**
  - `GET /`: Retrieves user's meal plans.
  - `POST /`: Creates a new meal plan.
- **/api/fitness-activities**
  - `GET /`: Retrieves user's fitness activities.
  - `POST /`: Logs a new fitness activity.
- **/api/goals**
  - `GET /`: Retrieves user's health goals.
  - `POST /`: Sets a new health goal.
  - `PUT /:goal_id`: Updates a specific goal.


## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HEBAMamdooh/laziz.git
   ```
2. **Install dependencies:**
   ```bash
   cd laziz
   pip install -r requirements.txt
   ```
3. **Set up the database:**
   - Create a MySQL database and update the database configuration in `config.py`.
   ```python
   DATABASE_URI = 'mysql+pymysql://username:password@localhost/laziz'
   ```
   - Run migrations to set up the tables.
   ```bash
   flask db upgrade
   ```
4. **Run the application:**
   ```bash
   flask run
   ```
5. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to Heba at hebamamdooh55@gmail.com.
