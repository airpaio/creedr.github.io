A QtPropertyBrowser Plugin for Qt Designer
##########################################

:date: 2017-01-17 07:47
:tags: qt, property browser, qtpropertybrowser, c++
:category: gui
:slug: qt-property-browser-plugin
:authors: Cory Robinson
:summary: Announcing a Qt 5.7 QtPropertyBrowser plugin fr Qt Designer

`Qt Solutions <https://github.com/qtproject/qt-solutions/tree/master/qtpropertybrowser>`_
implements a framework for a property browser like the one found in Qt Designer.
This particular implementation is for Qt 4, and doesn't seem to have much support
since the last commit was in early 2015.

There are some repos that have ported this code to work on Qt >=5.
`This <https://bitbucket.org/eligt/qtpropertybrowser>`_ bitbucket repo is one
such repo, and I can confirm that this code works for Qt 5.7 running on a
Linux machine.

I have taken the code from the bitbucket repo linked to above, and have written
a plugin to use the property browser with Qt Designer and Qt 5.7. You can
visit my `Github repo <https://github.com/creedr/QtPropertyBrowser>`_ to get
a clone of the qtpropertybrowser and the plugin to try it out for yourself.

Dragging the property browser widget onto your workspace is a bit unimpressive
since it's such a barebones object. The 'demo' example found in the
QtPropertyBrowser/examples directory shows a nice mix of uses for the widget,
and in a future post I will show an example of how I am using this widget.
