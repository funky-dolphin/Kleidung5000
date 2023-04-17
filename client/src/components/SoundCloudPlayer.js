import React from 'react';

const SoundCloudPlayer = ({ url }) => {
  return (
    <div className="soundcloud-player" style={{ display: 'none' }}>
      <iframe
        width="0%"
        height="0"
        scrolling="no"
        frameBorder="no"
        allow="autoplay"
        src={`${url}&auto_play=true&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false&visual=false`}
        title="Background SoundCloud Player"
      ></iframe>
    </div>
  );
};

export default SoundCloudPlayer;