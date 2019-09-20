<template>
  <!--Navbar-->
  <nav class="navbar navbar-expand-lg navbar-dark primary-color">
    <!-- Navbar brand -->
    <a class="navbar-brand" href="/">Vue-Flask</a>

    <!-- Collapse button -->
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#basicExampleNav"
      aria-controls="basicExampleNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <!-- Collapsible content -->
    <div class="collapse navbar-collapse" id="basicExampleNav">
      <!-- Links -->
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link class="nav-link" to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/about">About</router-link>
        </li>
      </ul>
      <!-- Links -->
      <ul class="navbar-nav ml-auto mr-4">
        <li class="nav-item">
          <router-link class="nav-link" to="/auth/login">Login</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/auth/register">Register</router-link>
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            id="navbarDropdownMenuLink"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >Accounts</a>
          <div class="dropdown-menu dropdown-primary" aria-labelledby="navbarDropdownMenuLink">
            <a class="dropdown-item" href="#">Profile</a>
            <a class="dropdown-item" href="#">Logout</a>
          </div>
        </li>
      </ul>
    </div>
    <!-- Collapsible content -->
  </nav>
  <!--/.Navbar-->
</template>