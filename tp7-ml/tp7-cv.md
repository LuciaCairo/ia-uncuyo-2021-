## create_folds() 

```
create_folds <- function(dataframe, nfolds) {
  x <- nrow(dataframe)/nfolds
  k <- ceiling(x) # Devuelve el primer entero mayor a x
  # Dividimos el dataframe en llos grupos
  lista <- split(dataframe,sample(rep(1:nfolds, k)))
  return(lista)
}
```

## cross_validation()

```
cross_validation <- function(dataframe, nfolds) {
  l <- create_folds(dataframe, nfolds)
  # seleccionamos la clase y las variables que nos interesan
  train_formula <- formula(inclinacion_peligrosa~altura+
                           Circ_tronco_cm+
                           Lat+long+
                           Seccion+
                           especie)
  # generamos el modelo 
  tree_model<-rpart(train_formula,data=data_train)
  # obtenemos la predicción
  p<-predict(tree_model,data_val,type='class') 
}
```
