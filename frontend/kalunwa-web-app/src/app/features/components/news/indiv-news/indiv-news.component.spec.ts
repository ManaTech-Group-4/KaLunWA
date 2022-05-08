import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, fakeAsync, inject, TestBed, tick } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { of } from 'rxjs';
import { routes } from 'src/app/app-routing.module';
import { NewsService } from '../service/news.service';

import { IndivNewsComponent } from './indiv-news.component';
const mockData =
{
    id: 4,
    title: "Project Name",
    date: "start date",
    image: {
      id: 27,
      image: "assets/images/event.jpg"
    },
    description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas. Commodo viverra maecenas accumsan lacus vel facilisis. Ut tristique et egestas quis ipsum. Scelerisque fermentum dui faucibus in. Amet risus nullam eget felis Ut ornare lectus sit amet. Volutpat consequat mauris nunc congue nisi vitae. Ut consequat semper viverra nam. At auctor urna nunc id cursus metus. Non odio euismod lacinia at quis risus sed vulputate odio. Nec dui nunc mattis enim ut. Augue neque gravida in fermentum. Turpis massa tincidunt dui ut ornare lectus sit. Vitae proin sagittis nisl rhoncus mattis. Sed risus pretium quam vulputate dignissim suspendisse. Quam nulla porttitor massa id neque aliquam vestibulum. Eu consequat ac felis donec et odio pellentesque diam. Vestibulum morbi blandit cursus risus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Fames ac turpis egestas sed tempus urna et pharetra pharetra. Tellus molestie nunc non blandit. Consequat mauris nunc congue nisi. Dignissim enim sit amet venenatis. Cras adipiscing enim eu turpis egestas pretium aenean pharetra magna. Nec ultrices dui sapien eget mi. Mattis pellentesque id nibh tortor. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Erat imperdiet sed euismod nisi porta lorem mollis. Odio morbi quis commodo odio aenean sed adipiscing. Auctor neque vitae tempus quam. Ipsum nunc aliquet bibendum enim facilisis gravida neque convallis. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Et malesuada fames ac turpis egestas. Commodo viverra maecenas accumsan lacus vel facilisis. Ut tristique et egestas quis ipsum. Scelerisque fermentum dui faucibus in. Amet risus nullam eget felis Ut ornare lectus sit amet. Volutpat consequat mauris nunc congue nisi vitae. Ut consequat semper viverra nam. At auctor urna nunc id cursus metus. Non odio euismod lacinia at quis risus sed vulputate odio. Nec dui nunc mattis enim ut. Augue neque gravida in fermentum. Turpis massa tincidunt dui ut ornare lectus sit. Vitae proin sagittis nisl rhoncus mattis. Sed risus pretium quam vulputate dignissim suspendisse. Quam nulla porttitor massa id neque aliquam vestibulum. Eu consequat ac felis donec et odio pellentesque diam. Vestibulum morbi blandit cursus risus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum."
  };

describe('IndivNewsComponent', () => {
  let component: IndivNewsComponent;
  let fixture: ComponentFixture<IndivNewsComponent>;
  let testBedService : NewsService;
  let mockNews = of(mockData);

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IndivNewsComponent ],
      imports: [RouterTestingModule.withRoutes(routes), HttpClientTestingModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    testBedService = TestBed.get(NewsService);
    fixture = TestBed.createComponent(IndivNewsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('Service injected via inject() and TestBed.get() should be the same instance (NewsService)',
    inject([NewsService], (injectService: NewsService) => {
      expect(injectService).toBe(testBedService);
  }));

  it('testing subscribe method is called',fakeAsync(() => {

    let eventDetailsSpy = spyOn(testBedService, 'getNewsDetails').and.returnValue(mockNews);
    let subSpy = spyOn(testBedService.getNewsDetails('4'), 'subscribe');
    component.ngOnInit();
    tick();
    expect(eventDetailsSpy).toHaveBeenCalledBefore(subSpy);
      expect(subSpy).toHaveBeenCalled();
  }));
});
