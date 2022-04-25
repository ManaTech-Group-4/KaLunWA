import { HttpClientTestingModule,} from '@angular/common/http/testing';
import { async, ComponentFixture, fakeAsync, inject, TestBed, tick } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { of } from 'rxjs/internal/observable/of';
import { AboutpageService } from '../../service/aboutpage.service';
import { AboutPageComponent } from './about-page.component';

const mockData = {'total_members' : 180};

describe('AboutPageComponent', () => {
  let component: AboutPageComponent;
  let fixture: ComponentFixture<AboutPageComponent>;
  let testBedService : AboutpageService;
  let mockDemographics = mockData;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AboutPageComponent ],
      imports : [ HttpClientTestingModule ],
      providers: [AboutpageService]

    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(AboutpageService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('Service injected via inject() and TestBed.get() should be the same (AboutpageService)',
    inject([AboutpageService], (injectService: AboutpageService) => {
      expect(injectService).toBe(testBedService);
  }));

  it('should expand history after click', async(() => {
    spyOn(component, 'onClick');
    const btn = fixture.debugElement.query(By.css('.button'));
    btn.triggerEventHandler('click', null);
    fixture.whenStable().then(() => {
    expect(component.onClick).toHaveBeenCalled();
    });
  }));

  it('testing subscribe method is called',fakeAsync(() => {
    let demographicsSpy = spyOn(testBedService, 'getDemographics').and.returnValue(of(mockDemographics));
      let subSpy = spyOn(testBedService.getDemographics(), 'subscribe');
    component.ngOnInit();
    tick();
    expect(demographicsSpy).toHaveBeenCalledBefore(subSpy);
      expect(subSpy).toHaveBeenCalled();
  }));


  it('should check if ShowMore is true after click',() => {
    component.onClick();
    expect(component.visible).toBe(true);
  });


  it('should be able to retrieve data from subscribe', done => {
    component.ngOnInit();
    const mockRetrieve$ = of(mockDemographics);

    mockRetrieve$.subscribe((total: any)=>{
      expect(total.total_members).toEqual(component.members.total_members);
      done();
    })
  });

});
