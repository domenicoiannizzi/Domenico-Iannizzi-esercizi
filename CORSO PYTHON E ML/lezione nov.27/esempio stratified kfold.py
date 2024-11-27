from sklearn.model_selection import StratifiedKFold

# Definizione di StratifiedKFold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Configurazione di RandomizedSearchCV con cv specificato
random_search_cv = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=10,
    scoring='accuracy',
    cv=cv,
    random_state=42,
    n_jobs=-1
)

# Esecuzione della ricerca
random_search_cv.fit(X, y)

# Migliori parametri trovati
print("Migliori parametri (con StratifiedKFold):")
print(random_search_cv.best_params_)