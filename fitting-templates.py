# john's fit
x = w
y = v

model = Model(func)
model.param_names
model.independent_vars

params = model.make_params(r0=10000,r1=200,r2=20,c=0)
result = model.fit(y, params, x=x)
plt.plot(x,result.best_fit)
plt.plot(x,y,'bo')
print(result.fit_report())

