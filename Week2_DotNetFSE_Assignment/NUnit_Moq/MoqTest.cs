
using Moq;
using NUnit.Framework;
public class EmployeeServiceTests {
    [Test]
    public void Test_Employee_Service_With_Mock() {
        var mockRepo = new Mock<IEmployeeRepo>();
        mockRepo.Setup(r => r.GetEmployeeCount()).Returns(5);
        Assert.AreEqual(5, mockRepo.Object.GetEmployeeCount());
    }
}
