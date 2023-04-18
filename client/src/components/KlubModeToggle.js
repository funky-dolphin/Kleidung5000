import React, { useState, useEffect } from 'react';
import classNames from 'classnames';
import moonIcon from './dark-theme-icon/moon.png';
import sunIcon from './dark-theme-icon/sun.png';
// need icons for 'moon' and 'sun' icon
const DarkModeToggle = () => {
  const [isDarkTheme, setIsDarkTheme] = useState(false);

  useEffect(() => {
    if (isDarkTheme) {
      document.body.classList.add('dark-theme');
    } else {
      document.body.classList.remove('dark-theme');
    }
  }, [isDarkTheme]);

  const toggleTheme = () => {
    setIsDarkTheme(!isDarkTheme);
  };

  return (
    <img
      id="color-mode"
      src={isDarkTheme ? moonIcon : sunIcon}
      alt="Toggle dark mode"
      onClick={toggleTheme}
      className={classNames({ 'dark-theme': isDarkTheme })}
    />
  );
};

export default DarkModeToggle;