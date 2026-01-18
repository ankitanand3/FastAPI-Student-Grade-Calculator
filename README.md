student-grade-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py                          # FastAPI app entry point & configuration
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── students.py              # Student CRUD endpoints
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py                    # App settings & environment variables
│   │   └── dependencies.py              # Reusable dependency injection
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py                   # Pydantic schemas for validation
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── grade_calculator.py          # Business logic for calculations
│   │
│   └── storage/
│       ├── __init__.py
│       └── student_store.py             # In-memory data storage
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                      # Pytest fixtures
│   ├── test_endpoints.py                # API endpoint tests
│   ├── test_grade_calculator.py         # Service layer tests
│   └── test_models.py                   # Pydantic model validation tests
│
├── .env                                  # Environment variables (don't commit!)
├── .gitignore                           # Git ignore rules
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation