import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { IndivProjectsModel } from '../../models/indiv-project-model';
import { ProjectItemService } from '../projects/service/project-item.service';

@Component({
  selector: 'app-indiv-project',
  templateUrl: './indiv-project.component.html',
  styleUrls: ['./indiv-project.component.scss']
})
export class IndivProjectComponent implements OnInit {

  project$: Observable<IndivProjectsModel>;

  constructor(private route: ActivatedRoute, private projectService: ProjectItemService) { }

  // project: IndivProjectsModel= {
  //   id: 1,
  //   title: "Project Name",
  //   tagline: "Tagline: Lorem ipsum dolor sit amet",
  //   start_date: "start date",
  //   camp: "Suba",
  //   status: "Past",
  //   cover_image: {
  //     id: 27,
  //     image: "assets/images/event.jpg"
  //   },
  //   description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas. Commodo viverra maecenas accumsan lacus vel facilisis. Ut tristique et egestas quis ipsum. Scelerisque fermentum dui faucibus in. Amet risus nullam eget felis Ut ornare lectus sit amet. Volutpat consequat mauris nunc congue nisi vitae. Ut consequat semper viverra nam. At auctor urna nunc id cursus metus. Non odio euismod lacinia at quis risus sed vulputate odio. Nec dui nunc mattis enim ut. Augue neque gravida in fermentum. Turpis massa tincidunt dui ut ornare lectus sit. Vitae proin sagittis nisl rhoncus mattis. Sed risus pretium quam vulputate dignissim suspendisse. Quam nulla porttitor massa id neque aliquam vestibulum. Eu consequat ac felis donec et odio pellentesque diam. Vestibulum morbi blandit cursus risus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas. Commodo viverra maecenas accumsan lacus vel facilisis. Ut tristique et egestas quis ipsum. Scelerisque fermentum dui faucibus in. Amet risus nullam eget felis Ut ornare lectus sit amet. Volutpat consequat mauris nunc congue nisi vitae. Ut consequat semper viverra nam. At auctor urna nunc id cursus metus. Non odio euismod lacinia at quis risus sed vulputate odio. Nec dui nunc mattis enim ut. Augue neque gravida in fermentum. Turpis massa tincidunt dui ut ornare lectus sit. Vitae proin sagittis nisl rhoncus mattis. Sed risus pretium quam vulputate dignissim suspendisse. Quam nulla porttitor massa id neque aliquam vestibulum. Eu consequat ac felis donec et odio pellentesque diam. Vestibulum morbi blandit cursus risus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum.",
  //   gallery:[
  //     {
  //       id: 1,
  //       image: "assets/images/event.jpg",
  //       thumbImage: "assets/images/event.jpg"
  //     },
  //     {
  //       id: 2,
  //       image: "assets/images/carousel/carousel1.jpg",
  //       thumbImage: "assets/images/carousel/carousel1.jpg"
  //     },
  //     {
  //       id: 3,
  //       image: "assets/images/carousel/carousel2.jpg",
  //       thumbImage: "assets/images/carousel/carousel2.jpg"
  //     },
  //     {
  //       id: 4,
  //       image: "assets/images/carousel/carousel3.jpg",
  //       thumbImage: "assets/images/carousel/carousel3.jpg"
  //     },
  //     {
  //       id: 5,
  //       image: "assets/images/carousel/carousel4.jpg",
  //       thumbImage: "assets/images/carousel/carousel4.jpg"
  //     },
  //     {
  //       id: 6,
  //       image: "assets/images/partners/partner1.jpeg",
  //       thumbImage: "assets/images/partners/partner1.jpeg"
  //     },
  //     {
  //       id: 7,
  //       image: "assets/images/carousel/carousel1.jpg",
  //       thumbImage: "assets/images/carousel/carousel1.jpg"
  //     },
  //     {
  //       id: 8,
  //       image: "assets/images/carousel/carousel2.jpg",
  //       thumbImage: "assets/images/carousel/carousel2.jpg"
  //     },
  //     {
  //       id: 9,
  //       image: "assets/images/carousel/carousel3.jpg",
  //       thumbImage: "assets/images/carousel/carousel3.jpg"
  //     },
  //     {
  //       id: 10,
  //       image: "assets/images/carousel/carousel4.jpg",
  //       thumbImage: "assets/images/carousel/carousel4.jpg"
  //     },
  //   ],
  //   contributors:[
  //     {
  //       id: 1,
  //       name: "partner_name",
  //       image: {
  //         id: 27,
  //         image: "assets/images/partners/partner1.jpeg"
  //       },
  //       category: "sponsor"
  //     },
  //     {
  //       id: 2,
  //       name: "partner_name",
  //       image: {
  //         id: 27,
  //         image: "assets/images/partners/partner1.jpeg"
  //       },
  //       category: "sponsor"
  //     },
  //     {
  //       id: 3,
  //       name: "partner_name",
  //       image: {
  //         id: 27,
  //         image: "assets/images/partners/partner1.jpeg"
  //       },
  //       category: "sponsor"
  //     },
  //     {
  //       id: 4,
  //       name: "partner_name",
  //       image: {
  //         id: 27,
  //         image: "assets/images/partners/partner1.jpeg"
  //       },
  //       category: "sponsor"
  //     },
  //   ]
  // }

  ngOnInit(): void {

    const projectId = this.route.snapshot.paramMap.get("id");
    this.project$ = this.projectService.getProjectDetails(projectId)
    .pipe(
      map((project: IndivProjectsModel) => ({
      id: project.id,
      title: project.title,
      image: project.image,
      description: project.description,
      start_date: project.start_date,
      camp: project.camp,
      status: project.status,
      gallery: project.gallery
        .map(imageSlide =>
          ({image: imageSlide.image,
            thumbImage: imageSlide.image,
            id: imageSlide.id
          })
        ),
      contributors: project.contributors
    })
));
    this.project$.subscribe(project => console.log(project));
  }

}
