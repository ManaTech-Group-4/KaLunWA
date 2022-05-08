import { Component, OnInit} from '@angular/core';
import { IndivCampModel } from 'src/app/features/models/indiv-camp-model';

@Component({
  selector: 'app-baybayon',
  templateUrl: './baybayon.component.html',
  styleUrls: ['./baybayon.component.scss'],
})
export class BaybayonComponent implements OnInit {

  constructor() { }

  camp: IndivCampModel={
    id: 1,
    theme_colors:{
      main: "#d9b863",
      background: "#ecdbb2",
      dark: "#965a39",
      comp: "#508594",
    },
    camp_name: "Baybayon",
    header_img: "assets/images/carousel/carousel2.jpg",
    tagline: "protect, safeguard, and preserve the purity of coastlines",
    socmed: {
      fb: "KL Camp Baybayon",
      twt_ig: "@klcampbaybayon",
    },
    content_image: {
      id:1,
      image: "assets/images/carousel/carousel2.jpg",
    },
    content: "The term Baybayon translates to Coasts. This camp is the prime unit that seeks to address issues involving our shores. They aim to protect, safeguard, and preserve the purity of coastlines.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas.",
    gallery: [
      {
        id: 1,
        image: "assets/images/event.jpg",
        thumbImage: "assets/images/event.jpg"
      },
      {
        id: 2,
        image: "assets/images/carousel/carousel1.jpg",
        thumbImage: "assets/images/carousel/carousel1.jpg"
      },
      {
        id: 3,
        image: "assets/images/carousel/carousel2.jpg",
        thumbImage: "assets/images/carousel/carousel2.jpg"
      },
      {
        id: 4,
        image: "assets/images/carousel/carousel3.jpg",
        thumbImage: "assets/images/carousel/carousel3.jpg"
      },
      {
        id: 5,
        image: "assets/images/carousel/carousel4.jpg",
        thumbImage: "assets/images/carousel/carousel4.jpg"
      },
      {
        id: 6,
        image: "assets/images/partners/partner1.jpeg",
        thumbImage: "assets/images/partners/partner1.jpeg"
      },
      {
        id: 7,
        image: "assets/images/carousel/carousel1.jpg",
        thumbImage: "assets/images/carousel/carousel1.jpg"
      },
      {
        id: 8,
        image: "assets/images/carousel/carousel2.jpg",
        thumbImage: "assets/images/carousel/carousel2.jpg"
      },
    ],
    events: [
      {
        id:1,
        image: "assets/images/carousel/carousel4.jpg",
        event_name: "Event Name1",
      },
      {
        id:2,
        image: "assets/images/carousel/carousel2.jpg",
        event_name: "Event Name2",
      },
      {
        id:3,
        image: "assets/images/carousel/carousel1.jpg",
        event_name: "Event Name3",
      },
      {
        id:4,
        image: "assets/images/carousel/carousel4.jpg",
        event_name: "Event Name4",
      },
      {
        id:5,
        image: "assets/images/partners/partner1.jpeg",
        event_name: "Event Name5",
      },
      {
        id:6,
        image: "assets/images/carousel/carousel3.jpg",
        event_name: "Event Name6",
      },
      {
        id:7,
        image: "assets/images/carousel/carousel2.jpg",
        event_name: "Event Name7",
      },
      {
        id:8,
        image: "assets/images/carousel/carousel1.jpg",
        event_name: "Event Name8",
      },
    ],
    projects: [
      {
        id:1,
        image: "assets/images/carousel/carousel4.jpg",
        project_name: "Project Name1",
      },
      {
        id:2,
        image: "assets/images/carousel/carousel2.jpg",
        project_name: "Project Name2",
      },
      {
        id:3,
        image: "assets/images/carousel/carousel1.jpg",
        project_name: "Project Name3",
      },
      {
        id:4,
        image: "assets/images/carousel/carousel4.jpg",
        project_name: "Project Name4",
      },
      {
        id:5,
        image: "assets/images/partners/partner1.jpeg",
        project_name: "Project Name5",
      },
      {
        id:6,
        image: "assets/images/carousel/carousel3.jpg",
        project_name: "Project Name6",
      },
      {
        id:7,
        image: "assets/images/carousel/carousel2.jpg",
        project_name: "Project Name7",
      },
      {
        id:8,
        image: "assets/images/carousel/carousel1.jpg",
        project_name: "Project Name8",
      },
    ],
  }

  ngOnInit(): void {
  }

}
