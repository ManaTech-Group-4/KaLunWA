import { Component, OnInit } from '@angular/core';
import { IndivEventsModel } from '../../models/indiv-event-model';
import { OwlOptions } from 'ngx-owl-carousel-o';

@Component({
  selector: 'app-indi-event',
  templateUrl: './indi-event.component.html',
  styleUrls: ['./indi-event.component.scss']
})
export class IndiEventComponent implements OnInit {

  constructor() { }

  event: IndivEventsModel= {
    id: 1,
    title: "Event Name",
    tagline: "Tagline: Lorem ipsum dolor sit amet",
    start_date: "start date",
    end_date: "end date",
    camp: "Suba",
    status: "Past",
    cover_image: {
      id: 27,
      image: "assets/images/event.jpg"
    },
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas. Commodo viverra maecenas accumsan lacus vel facilisis. Ut tristique et egestas quis ipsum. Scelerisque fermentum dui faucibus in. Amet risus nullam eget felis Ut ornare lectus sit amet. Volutpat consequat mauris nunc congue nisi vitae. Ut consequat semper viverra nam. At auctor urna nunc id cursus metus. Non odio euismod lacinia at quis risus sed vulputate odio. Nec dui nunc mattis enim ut. Augue neque gravida in fermentum. Turpis massa tincidunt dui ut ornare lectus sit. Vitae proin sagittis nisl rhoncus mattis. Sed risus pretium quam vulputate dignissim suspendisse. Quam nulla porttitor massa id neque aliquam vestibulum. Eu consequat ac felis donec et odio pellentesque diam. Vestibulum morbi blandit cursus risus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas. Commodo viverra maecenas accumsan lacus vel facilisis. Ut tristique et egestas quis ipsum. Scelerisque fermentum dui faucibus in. Amet risus nullam eget felis Ut ornare lectus sit amet. Volutpat consequat mauris nunc congue nisi vitae. Ut consequat semper viverra nam. At auctor urna nunc id cursus metus. Non odio euismod lacinia at quis risus sed vulputate odio. Nec dui nunc mattis enim ut. Augue neque gravida in fermentum. Turpis massa tincidunt dui ut ornare lectus sit. Vitae proin sagittis nisl rhoncus mattis. Sed risus pretium quam vulputate dignissim suspendisse. Quam nulla porttitor massa id neque aliquam vestibulum. Eu consequat ac felis donec et odio pellentesque diam. Vestibulum morbi blandit cursus risus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum.",
    gallery: [
      {
        id: 1,
        image: "assets/images/event.jpg"
      },
      {
        id: 2,
        image: "assets/images/carousel/carousel1.jpg"
      },
      {
        id: 3,
        image: "assets/images/carousel/carousel2.jpg"
      },
      {
        id: 4,
        image: "assets/images/carousel/carousel3.jpg"
      },
      {
        id: 5,
        image: "assets/images/carousel/carousel4.jpg"
      },
      {
        id: 6,
        image: "assets/images/partners/partner1.jpeg"
      },
    ],
    contributors:[
      {
        id: 1,
        name: "partner_name",
        image: {
          id: 27,
          image: "assets/images/partners/partner1.jpeg"
        },
        category: "sponsor"
      },
      {
        id: 2,
        name: "partner_name",
        image: {
          id: 27,
          image: "assets/images/partners/partner1.jpeg"
        },
        category: "sponsor"
      },
      {
        id: 3,
        name: "partner_name",
        image: {
          id: 27,
          image: "assets/images/partners/partner1.jpeg"
        },
        category: "sponsor"
      },
      {
        id: 4,
        name: "partner_name",
        image: {
          id: 27,
          image: "assets/images/partners/partner1.jpeg"
        },
        category: "sponsor"
      },
    ]
  }
  customOptions: OwlOptions = {
    loop: true,
    //margin: 100,
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
        items: 5
      }
    },
    nav: true
  }

  ngOnInit(): void {
  }
}
