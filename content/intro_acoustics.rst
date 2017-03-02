An Introduction to Acoustics
############################

:date: 2017-2-16 22:46
:tags: acoustics
:category:
:slug: an_introduction_to_acoustics
:summary:
:status: draft


As a geophysicist, I work with data every day that has its roots buried in
the wave equation. I became quite familiar with the wave equation and several
applications of it while I was in grad school, and the math can get pretty hairy,
especially from a numerical analysis standpoint. An application of the wave
equation of particular interest to me is in acoustics.

Acoustics, not only deals with sounds that we can hear, but in general can be
regarded as mechanical waves that can pass through solids, liquids, and gases.
Of course we can hear acoustic waves such as the sound of a tree falling in a
forest. We may even feel the low frequency vibrations of the base guitar
passing through our body at a rock concert. We can also see an image of
acoustic waves when we look at a baby with an ultrasound machine. An explosive
energy source on the surface of the Earth sends acoustic waves through the
Earth, and we can record the signals of the waves reflecting off of the
different layers of rock below the Earth's surface.

Analyzing acoustic waves can be done by studying the physical propagation
of the wave, or by turning to the frequency spectrum for a signal processing
treatment of the acoustic waveform. There are way too many applications to
mention here, so I will point you to the
`Wikipedia <https://en.wikipedia.org/wiki/Acoustics>`_ page on acoustics to
get a better feel for the history and applications.

My goal is for this to serve as an introduction for a series of posts that I
will make regarding applications of acoustics that I find interesting.
We will start with a derivation of the acoustic wave equation from the
Conservation Laws, and then move into numerical analysis and simulation of
wave propagation which will have a somewhat detailed treatment of scientific
computing, and then finally move into some other interesting applications
of acoustics.



Conservation Laws
=================
Acoustical systems, as well as most applications in science and engineering,
are governed by the conservation laws such as the conservation of mass which
says that mass cannot be either created or destroyed in a closed system. A
closed system could be anything from a microscopic system up to the scale of
our whole universe.


Mass
----
For our acoustics problem, we will begin by considering
the conservation of mass in a compressible fluid, and in particular, flow
through a tube of gas where the density and velocity of the gas remains constant
throughout. Considering this is a one-dimensional tube with space variable
:math:`x`, let :math:`\rho(x,t)` represent density, and :math:`v(x,t)`
represent velocity at point :math:`x` and time :math:`t`. Then we can
measure the total mass :math:`m` in the tube with the integral

.. math::
    \int_{x_1}^{x_2} \rho(x,t)dx = m.

Let's assume that the gas tube is a closed system, except at the endpoints
where mass can be changed only if gas were flowing in or out of the endpoints.
This is refereed to as *mass flux*, which we will write as :math:`F`, i.e.

.. math::
    F = \rho(x,t)v(x,t).

Taking the time derivative of the total mass, we have

.. math::
    \frac{d}{dt}\int_{x_1}^{x_2} \rho(x,t)dx = F(x_1, t) - F(x_2, t) +
    \int_{x_1}^{x_2} S(x,t)dx

where :math:`S` is a source or sink term where mass can be injected or removed
from the system. This is an *integral form* of the **conservation of mass law**.

Assuming that :math:`\rho` and :math:`F` have continuous derivatives, then we
can rewrite the integral form (with subscripts indicating partial derivatives)
as

.. math::
    \int_{x_1}^{x_2} \rho_t(x,t)dx = -\int_{x_1}^{x_2}F_x(x,t)dx +
    \int_{x_1}^{x_2} S(x,t)dx

    \implies \int_{x_1}^{x_2} (\rho_t + F_x - S)dx = 0

and thus the integrand must be :math:`0` for all :math:`x_1 \text{and } x_2.`
This leaves us with

.. math::
    \rho_t + (\rho v)_x = S

which is the *differential form* of the **conservation of mass law**.


Momentum
--------
It follows from Newton's Second Law of Motion that *momentum* is the
product of mass and velocity. The *total momentum* can be written similarly
to that of mass as

.. math::
    \int_{x_1}^{x_2} \rho v dx = mv

For the *momentum flux*, we have two contributions.

1.  Similar to the mass flux, momentum can be carried by the velocity of moving
fluids, and this contribution is written as the product of momentum and
velocity, i.e. :math:`(\rho v)v = \rho v^2`

2.  There is a flux due to pressures and stresses on the fluid such as
viscosity. We will neglect the viscous stress for now, but since acoustics
deals with pressure fluctuations, we will keep the *pressure* term written as
:math:`p`

Combining the two flux contributions, we write the *momentum flux* as

.. math::
    G = \rho v^2 + p.

We can write the *integral form* of the **conservation of momentum law** as

.. math::
    \frac{d}{dt}\int_{x_1}^{x_2} \rho v dx = G(x_1,t) - G(x_2,t) +
    \int_{x_1}^{x_2} S(x,t),

and taking the same steps as we did with the mass law, we arrive at the
*differential form* of the **conservation of momentum law**

.. math::
    (\rho v)_t + (\rho v^2 + p)_x = S


Energy
------
*Total energy*, :math:`E` is written as the sum of *internal energy*,
:math:`\rho e`, and *kinetic energy* :math:`\frac{1}{2}\rho v^2`,

.. math::
    E = \rho e + \frac{1}{2}\rho v^2.

We use the *constitutive relation* (which we will revisit again shortly)
:math:`e` written as a function of pressure and density, i.e.
:math:`e = e(p,\rho)` under the assumption that the gas is in chemical and
thermodynamic equilibrium. This is also called the *equation of state.*

Similar to the momentum flux, we have two contributions to the *energy flux.*
We have energy being carried by the fluid, :math:`Ev`, and pressure being
carried by the fluid, :math:`pv`. We write the energy flux :math:`H` as

.. math::
    H = Ev + pv

Now the *integral form of the **conservation of energy law** is

.. math::
    \frac{d}{dt}\int_{x_1}^{x_2} E dx = H(x_1,t) - H(x_2,t) +
    \int_{x_1}^{x_2} S(x,t) dx

and it follows that the *differential form* is written as

.. math::
    E_t + [(E+p)v]_x = S.



Constitutive Relations
======================
*The Quest for the Speed of Sound*
----------------------------------
