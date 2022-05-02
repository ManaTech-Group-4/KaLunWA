import { Component, OnInit } from '@angular/core';
import { IndivCampModel } from 'src/app/features/models/indiv-camp-model';
import { OwlOptions } from 'ngx-owl-carousel-o';

@Component({
  selector: 'app-lasang',
  templateUrl: './lasang.component.html',
  styleUrls: ['./lasang.component.scss']
})
export class LasangComponent implements OnInit {

  constructor() { }

  camp: IndivCampModel={
    id: 1,
    theme_colors:{
      main: "#3f6218",
      background: "#9ABA77",
      dark: "#233620",
      comp: "#481A1A",
    },
    camp_name: "Lasang",
    header_img: "assets/images/carousel/carousel2.jpg",
    tagline: "spearhead measures that conserve, manage, and develop our woodlands",
    socmed: {
      fb: "KL Camp Lasang",
      twt_ig: "@klcamplasang",
    },
    content_image: {
      id:1,
      image: "assets/images/carousel/carousel2.jpg",
    },
    content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas.",
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
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:2,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:3,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:4,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:5,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
    ],
    projects: [
      {
        id:1,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:2,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:3,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:4,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
      {
        id:5,
        image: "assets/images/camps/baybayon/trashtag.jpg",
        event_name: "Event Name",
      },
    ],
  }

  customOptions: OwlOptions = {
    loop: true,
    mouseDrag: false,
    touchDrag: false,
    pullDrag: false,
    dots: false,
    navSpeed: 700,
    navText: ['', ''],
    responsive: {
      0: {
        items: 1
      },
      400: {
        items: 2
      },
      740: {
        items: 3
      },
      940: {
        items: 4
      }
    },
    nav: true
  }

  ngOnInit(): void {
  }

}
