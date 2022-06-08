from flask import Flask, render_template, request, flash, url_for, redirect
@app.route('/')
def serverList():  # put application's code here
    return render_template('servers.html', servers=Servers.query
                           )


@app.route('/create', methods= ['GET', 'POST'])
def createserver():
    form = ServersForm()

    if form.validate_on_submit():

        new_reg = Servers(request.form['SiteName'], request.form['serverName'], request.form['IPAddress'], request.form['OS'],\
                          request.form['HOST_IP'], request.form['HOSTType'], request.form['HOST_ILOM_IP'])
        db.session.add(new_reg)
        db.session.commit()

        flash("Registration was succussfull")
        return redirect(url_for('success'))
    return render_template('CreateServer.html', form=form)



@app.route('/serverview')
def results():
    return Servers.query.filter_by(serverName="Exchange").one()


@app.route('/success')
def success():
    return render_template('Success.html')

if __name__ == '__main__':
    app.run()
