<template>
  <svg
    class="anime-scene"
    viewBox="0 0 1600 720"
    preserveAspectRatio="xMidYMid slice"
    role="img"
    aria-label="樱花月夜的二次元风景"
  >
    <defs>
      <linearGradient id="sky" x1="0" x2="0" y1="0" y2="1">
        <stop stop-color="#9e6d9f" />
        <stop offset=".46" stop-color="#e8a1b9" />
        <stop offset="1" stop-color="#ffd4c9" />
      </linearGradient>
      <linearGradient id="horizon" x1="0" x2="0" y1="0" y2="1">
        <stop stop-color="#a96c91" />
        <stop offset="1" stop-color="#503c70" />
      </linearGradient>
      <linearGradient id="water" x1="0" x2="0" y1="0" y2="1">
        <stop stop-color="#80668c" />
        <stop offset="1" stop-color="#292c55" />
      </linearGradient>
      <radialGradient id="moon">
        <stop stop-color="#fff8e5" />
        <stop offset=".75" stop-color="#ffead2" />
        <stop offset="1" stop-color="#ffd2c7" stop-opacity="0" />
      </radialGradient>
      <filter id="glow"><feGaussianBlur stdDeviation="9" /></filter>
      <filter id="soft"><feGaussianBlur stdDeviation="3" /></filter>
    </defs>
    <rect width="1600" height="720" fill="url(#sky)" />
    <circle cx="1200" cy="150" r="185" fill="url(#moon)" filter="url(#soft)" />
    <circle cx="1200" cy="150" r="78" fill="#fff1d7" opacity=".9" />
    <g fill="#fff1ea" opacity=".32" filter="url(#soft)">
      <path
        d="M150 174c45-58 115-50 140-4 45-21 101 17 89 67H109c-17-28 7-58 41-63Z"
      />
      <path
        d="M1240 285c35-48 91-37 107-2 39-18 79 13 71 50h-245c-10-24 14-43 35-48Z"
      />
    </g>
    <path
      d="M0 400c160-85 275-91 414-8 120-83 258-105 410-13 143-90 293-74 414-8 135-92 264-97 362-34v383H0Z"
      fill="url(#horizon)"
    />
    <path
      d="M0 466c217-48 356-30 541 35 153-70 284-72 458 0 183-76 371-71 601-10v239H0Z"
      fill="url(#water)"
    />
    <g fill="none" stroke="#f9c4ce" opacity=".28">
      <path d="M650 535c220 25 390 25 600 0" />
      <path d="M718 568c182 20 330 19 502 0" />
      <path d="M770 600c118 12 235 13 347 0" />
    </g>
    <g fill="#201f42">
      <path
        d="M0 720V190c54 42 109 90 142 171 42-66 81-111 134-145-22 122-16 198 37 273-72 74-104 148-111 231Z"
      />
      <path
        d="M1600 720V121c-73 61-116 136-138 229-34-60-82-108-127-140 25 120 8 211-46 306 76 70 110 125 117 204Z"
      />
    </g>
    <g fill="#29213d">
      <path d="M139 720c22-141 105-239 183-286l60 34c-42 90-58 167-42 252Z" />
      <path d="M1365 720c-13-149-76-244-160-292l-47 36c35 85 42 171 26 256Z" />
    </g>
    <g transform="translate(1015 410)">
      <path d="M0 214V79l112-79 151 80v134Z" fill="#704d65" />
      <path d="M-22 85 112-19l177 105-26 22-151-81L0 111Z" fill="#f7c2cc" />
      <path d="M81 214v-94h63v94" fill="#3b3152" />
      <path d="M183 106h40v53h-40Z" fill="#ffd6d0" />
      <path d="M194 120h18" stroke="#b7798d" stroke-width="4" />
      <path d="M247 77V28h13v57" stroke="#ffc3cb" stroke-width="7" />
      <circle cx="258" cy="25" r="9" fill="#ffdae2" />
    </g>
    <g transform="translate(130 212)">
      <path
        d="M77 173c-7-85 19-140 66-168 37 52 46 112 6 195Z"
        fill="#3f3156"
      />
      <circle cx="125" cy="94" r="40" fill="#ffd9cc" />
      <path
        d="M80 87C72 31 108 0 152 19c41 18 42 64 12 94-4-34-18-54-41-64-10 28-25 40-43 38Z"
        fill="#453458"
      />
      <path
        d="M109 98h9m26 0h9"
        stroke="#6d4565"
        stroke-width="4"
        stroke-linecap="round"
      />
      <path
        d="M119 122q9 7 18 0"
        stroke="#d47a92"
        stroke-width="3"
        fill="none"
      />
      <path d="M88 168q36-22 72 0l29 48H63Z" fill="#f6a5bc" />
      <path
        d="m80 164-43 44m114-44 42 44"
        stroke="#f8bdc6"
        stroke-width="11"
        stroke-linecap="round"
      />
    </g>
    <g fill="#ffdbe0" opacity=".95">
      <circle cx="180" cy="293" r="8" />
      <circle cx="245" cy="354" r="6" />
      <circle cx="342" cy="259" r="9" />
      <circle cx="1430" cy="260" r="7" />
      <circle cx="1490" cy="326" r="10" />
      <circle cx="1340" cy="218" r="6" />
    </g>
    <g fill="#fff1b8" opacity=".75" filter="url(#glow)">
      <circle cx="550" cy="430" r="8" />
      <circle cx="884" cy="376" r="7" />
      <circle cx="1270" cy="420" r="8" />
      <circle cx="420" cy="503" r="5" />
    </g>
  </svg>
</template>
